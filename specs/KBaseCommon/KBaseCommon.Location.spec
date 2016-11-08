/*
Information about a location.
lat - latitude of the site, recorded as a decimal number. North latitudes
    are positive values and south latitudes are negative numbers.
lon - longitude of the site, recorded as a decimal number. West
    longitudes are positive values and east longitudes are negative
    numbers.
elevation - elevation of the site, expressed in meters above sea level.
    Negative values are allowed.
date - date of an event at this location (for example, sample
    collection), expressed in the format YYYY-MM-DDThh:mm:ss.SSSZ
description - a free text description of the location and, if applicable,
    the associated event.

@optional date description
*/
typedef structure {
  float lat;
  float lon;
  float elevation;
  string date;
  string description;
} Location;