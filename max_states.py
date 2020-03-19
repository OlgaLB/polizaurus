#!/usr/bin/env python3

import xml.etree.ElementTree
import xmltodict
import json

import os

import argparse

import shapely.wkt
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def map_location_to_state(input_xml, states):
    """
        Creates a dictionary of locations and states they belong to.
        
        Parameters:
            input_xml : str
                Path to xml file with locations and their latitude, longitude.
            states : list of str
                List of files with state coordinates
         
        Output:
            mapped_states : dict
                Dictionary of mapped locations and states
    """
    # dictionary to save location:state pairs
    mapped_states = {}
    # root element within input xml file that contains location, latitude and longitude
    root = xml.etree.ElementTree.parse(input_xml).getroot()

    # for each file from states list
    for filename in states:
        # open file with state coordinates for reading
        with open(filename, 'r') as content_file:
            # read and save content of the file with state coordinates
            coordinates = content_file.read()
            # create polygon object using coordinates that were read and saved above
            polygon = shapely.wkt.loads(coordinates)

            # for each location element from input xml file
            for type_tag in root.findall('Location'):
                # if location as a key is not yet in the dictionary - add it with 'null' value for now
                if type_tag.text not in mapped_states.keys():
                    mapped_states.update({type_tag.text: 'null'})
                # get and save latitute
                value_x = type_tag.get("latitude")
                # get and save longitude
                value_y = type_tag.get("longitude")
                # create point object using coordinates that were read and saved above
                point = Point(float(value_y),float(value_x))
                # check whether point belongs to polygon
                if (point.within(polygon)):
                # if the point belongs to the polygon,
                # add a key:value pair to the dictionary,
                # where key is location element from input xml file,
                # value is filename of the .wkt state file without folder name and without extension
                    mapped_states[type_tag.text] = os.path.splitext(filename.split("/")[-1])[0]
    return mapped_states


def create_json(output_json, mapped_states):
    """
        Creates a json file with the mapped locations and states.
        
        Parameters:
            output_json : str
                Path to json file to be created.
            mapped_states : dict
                Dictionary of data to be written to the json file.
    """
    # open file with for writing
    with open(output_json, 'w', encoding='utf-8') as mapped_json:
        # write dictionary to the file as a json
        # using indentation, sorting by key (location)
        json.dump(mapped_states, mapped_json, indent = 4, sort_keys = True, ensure_ascii = False)


if __name__ == '__main__':
    args_to_parse = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)

    # xml file with locations and coordinates
    args_to_parse.add_argument('--input', required=True)
    # folder with states polygon coordinates
    # associate list of files with --states argument
    args_to_parse.add_argument('--states', nargs='+', required=True)
    # json file with locations mapped to states
    args_to_parse.add_argument('--output', required=True)

    args = args_to_parse.parse_args()

    mapped_states = map_location_to_state(args.input, args.states)
    create_json(args.output, mapped_states)
