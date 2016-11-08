
import os
import codecs
import json
import datetime

from git import Repo


from biokbase.workspace.client import Workspace


WS_URL = {
    'ci': 'https://ci.kbase.us/services/ws',
    'appdev': 'https://appdev.kbase.us/services/ws',
    'next': 'https://next.kbase.us/services/ws',
    'prod': 'https://kbase.us/services/ws'
}

BASEDIR = '../'


def main():

    endpoint = 'ci'

    ws = Workspace(WS_URL[endpoint])
    target_dir = os.path.abspath('../specs')
    repo = Repo(os.path.abspath('../'))

    # create the manifest
    manifest = Manifest(os.path.abspath('../manifest.json'))
    manifest.set_ws_url(WS_URL[endpoint])

    modules = [
        'DataPalette',
        'GenomeComparison',
        'KBaseAssembly',
        'KBaseBiochem',
        'KBaseCommon',
        'KBaseFBA',
        'KBaseFeatureValues',
        'KBaseFile',
        'KBaseGeneFamilies',
        'KBaseGenomeAnnotations',
        'KBaseGenomes'
        'KBaseNarrative',
        'KBaseOntology',
        'KBasePhenotypes',
        'KBaseRNASeq',
        'KBaseSets',
        'KBaseTrees',
        'ProbabilisticAnnotation'
    ]

    for m in modules:
        try:
            mu = ModuleUpdater(ws, m, target_dir, repo)
            mu.update(manifest)
        except Exception as e:
            print(str(e))




def log(message):
    print(message)



class Manifest:

    _MODULES = 'modules'
    _TYPES = 'types'

    def __init__(self, path):
        self.path = path
        self.manifest = {}
        self.original_manifest_data = ''
        if os.path.isfile(path):
            with open(self.path, 'r') as manifest_file:
                self.original_manifest_data = manifest_file.read()
            manifest_file.close()
            self.manifest = json.loads(self.original_manifest_data)
            self._initialize_modules()
        else:
            self._initialize_modules()
            self.save()


    def _to_json_string(self):
        return json.dumps(self.manifest, sort_keys=True,
                          indent=4, separators=(',', ': '))

    def is_modified(self):
        if self.original_manifest_data == self._to_json_string():
            return False
        return True


    def save(self):
        manifest_data = self._to_json_string()
        with codecs.open(self.path, 'w', 'utf-8') as manifest_file:
            manifest_file.write(manifest_data)
        manifest_file.close()


    def set_ws_url(self, url):
        if 'url' in self.manifest:
            if self.manifest['_url'] == url:
                return
            else:
                raise ValueError('Cannot set url to:' + str(url) +
                                 ' , manifest is already set to: ' +
                                 str(self.manifest['url']))
        self.manifest['_url'] = url


    def _initialize_modules(self):
        if self._MODULES not in self.manifest:
            self.manifest['modules'] = {}


    def set_module_version(self, module, version, chsum, owners, types):
        ts = datetime.datetime.fromtimestamp(int(version) / 1000).strftime('%Y-%m-%d %H:%M:%S')
        if module not in self.manifest[self._MODULES]:
            self.manifest[self._MODULES][module] = {'types': []}
        self.manifest[self._MODULES][module]['_version'] = version
        self.manifest[self._MODULES][module]['_timestamp'] = ts
        self.manifest[self._MODULES][module]['_chsum'] = chsum
        self.manifest[self._MODULES][module]['owners'] = sorted(owners)
        self.manifest[self._MODULES][module]['types'] = types


    def get_module_version(self, module):
        if module in self.manifest[self._MODULES]:
            return self.manifest[self._MODULES][module]['_version']
        return 0


    def get_module_latest_types(self, module):
        if module in self.manifest[self._MODULES]:
            return self.manifest[self._MODULES][module]['types']
        return []


    def get_module_commit_message(self, module):
        if module not in self.manifest[self._MODULES]:
            raise ValueError('Cannot generate commit message for ' + module + ' as it is not in manifest.')

        version = self.manifest[self._MODULES][module]['_version']
        ts = self.manifest[self._MODULES][module]['_timestamp']
        return 'Updated ' + module + ' to ' + str(version) + ' (' + ts + ')'




class ModuleUpdater:

    def __init__(self, ws, module_name, target_dir, repo):
        self.ws = ws
        self.module_name = module_name
        self.target_dir = target_dir
        self.repo = repo


    def update(self, manifest):
        '''
        we want to iterate over all the versions and add each one as a separate
        commit.  That way we can see how each type was updated.
        '''
        vers = self.ws.list_module_versions({'mod': self.module_name})['vers']
        vers.sort()
        latest_version_in_manifest = manifest.get_module_version(self.module_name)


        # for each module version
        for version in vers:
            if version <= latest_version_in_manifest:
                print('skipping ' + self.module_name + ' - ' + str(version) + ', already up to date')
                continue

            # 1) get module info
            log('updating ' + self.module_name + ' - ' + str(version))
            module_info = self.ws.get_module_info({'mod': self.module_name, 'ver': version})

            # 2) write out the spec file
            module_path = os.path.join(self.target_dir, self.module_name)
            module_spec_filename = self.module_name + '.spec'
            self.write_file(module_path, module_spec_filename, module_info['spec'])

            # 3) update the module version manifest
            types = list(module_info['types'])
            latest_module_types = manifest.get_module_latest_types(self.module_name)
            manifest.set_module_version(self.module_name, version, module_info['chsum'], module_info['owners'], types)

            # 4) commit the change
            manifest.save()
            module_spec_path = os.path.join(module_path, module_spec_filename)
            self.add_files_and_commit(
                [module_spec_path, manifest.path],
                manifest.get_module_commit_message(self.module_name))

            # 4) iterate over each type and save / commit the change
            for type_string in types:
                if type_string in latest_module_types:
                    #log(' - no changes for ' + type_string)
                    continue

                log(' - updating ' + type_string)
                # get the type info, write the spec out, and commit the change
                type_info = self.ws.get_type_info(type_string)
                type_spec_filename = type_string.split('-')[0] + '.spec'
                self.write_file(module_path, type_spec_filename, type_info['spec_def'])
                self.add_files_and_commit(
                    [os.path.join(module_path, type_spec_filename)],
                    'Updated type to ' + type_string)


    def write_file(self, path, filename, content):
        fullpath = os.path.join(path, filename)
        log(' --- writing ' + fullpath)
        if not os.path.isdir(path):
            os.makedirs(path)
        with codecs.open(fullpath, 'w', 'utf-8') as file:
            file.write(content)
        file.close()


    def add_files_and_commit(self, filepaths, commit_message):
        log(' --- committing - ' + commit_message)
        self.repo.index.add(filepaths)
        self.repo.index.commit(commit_message)



if __name__ == '__main__':
    main()
