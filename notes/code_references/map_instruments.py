
def retrieve_scale(client_input):
        front_unit, raw_scale = client_input.split(":")
        if "," in raw_scale:
            temp_scale = raw_scale.split(",")
            temp_join = ("").join(temp_scale)
            cleaned_scale = int(temp_join)   
        else:
            cleaned_scale = int(raw_scale)
        return cleaned_scale

def map_scale():
     
    CONSTANTS = {"cm": {"km": 0.00001,
                        "mi": 0.0000062137,
                        "nm": 0.0000053996},
                
            "in": {"km": 0.0000254,
                   "mi": 0.000015783,
                   "nm":  0.000013715}}
                
    CONSTANTS_REVERSE = {"km": {"cm": 100_000,
                                "in": 39_370.08},

                "mi": {"cm": 160_934.4,
                      "in": 63_360},

                "nm": {"cm": 185_200,
                      "inc": "72_913.39"}}
    
    mapscale_input = input("What is your map scale. Please format in `1:x` ")
    scale = retrieve_scale(mapscale_input)  

    for outer_key in CONSTANTS.keys():
        for key, value in CONSTANTS[outer_key].items():
            print(f"At a scale of 1:{scale:,}: 1 {outer_key} on the map equals {value*scale:.3f} {key} on the ground. ")
    

def ground_distance():
     
    IN_CM = {"in": {"cm": 2.54},
             "cm": {"in": 1/2.54}}

    map_distance = int(input("What is the map distance? "))
    map_distance_unit = input("What is the map unit? Choose 'in' or 'cm' ")
    ground_distance = int(input("What is the ground distance? " ))
    ground_distance_unit = input("What is the ground distance unit? Choose 'mi' ")


def main():                    

    print("Welcome to Map Instruments")
    selection = input("Choose between 'map scale' or 'map ground distance'")

    if selection ==  "map scale":
        map_scale()

    #if selection == "map ground distance":
    #     ground_distance() 
         

    
main()


