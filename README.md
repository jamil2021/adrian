# Azimuth, Elevation, and Slant Range Calculator

This Python script calculates the ground distance, bearing, elevation angle, and slant range distance between two given locations.

## Overview

The purpose of this program is to determine the position of a drone, aircraft, or satellite relative to another known position. It utilizes the Haversine formula to calculate the ground distance between the two locations and basic trigonometry to compute the bearing, elevation angle, and slant range distance.

## Features

- Calculates ground distance between two points on Earth (downrange distance).
- Determines the bearing in true degrees from North between the two points.
- Calculates the elevation angle in true degrees from North between the two points.
- Computes the slant range distance between the two points in meters.

## Usage

1. Run the script `az_el_slant.py`.
2. Enter the latitude, longitude, and elevation of the first location.
3. Enter the latitude, longitude, and elevation of the second location.
4. The script will output the calculated values including bearing, elevation angle, downrange distance, and slant range distance.

## Inputs

- Latitude and longitude coordinates of the two locations in decimal degrees.
- Elevation of the two locations in meters.

## Example

Location 1:
- Latitude: -34.0973
- Longitude: 150.7796
- Elevation: 210 meters

Location 2:
- Latitude: -25.1765
- Longitude: 148.4382
- Elevation: 810000 meters

## Output

From Location 1 to Location 2:
- Bearing Degrees (True North): [computed bearing]
- Elevation in Degrees: [computed elevation angle]
- Down Range in Meters: [computed downrange distance]
- Slant Range in Meters: [computed slant range distance]

## Acknowledgments

- This script is inspired by the need to calculate the position of drones, aircraft, and satellites relative to known positions.
- Special thanks to the authors of the Haversine formula and trigonometric principles used in this script.

