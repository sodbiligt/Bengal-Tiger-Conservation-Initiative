from core import Tiger, Habitat, Poaching, Prey, Data, Protection, Tourist
def test_tiger_init():
    # Test that we can initialize tigers
    tiger = Tiger("Tony", 190, 3.0, "Healthy", 100) #filler code
    assert tiger. name == "Tony", "Tigers name should be set to Tony" #filler code
    assert tiger.weight == 190, "Tigers weight should be set to 190"#filler code
    print("Init Tiger was successful")
def test_habitat_init():
    habitat = Habitat("South Asia", "High", "Rainforest", "Protected", 50, "Moderate") #filler code
    assert habitat.location == "South Asia", "Habitat location should be South Asia"#filler code
    print ("Init habitat was successful")
def test_poaching_init():
    poaching = Poaching("2024-11-20", "Trapping", "Tony") #filler code
    assert poaching.date == "2024-11-20", "Poaching date should be 2024-11-20"#filler code
    print("Init Poaching was successful")
def test_prey_init():
    prey = Prey("Panthera tigris", "South Asia") #filler code
    assert prey.sci_name == "Panthera tigris","Prey scientific name should be Panthera tigris"#filler code
    print("Init Prey was successful")
def test_data_init():
    data = Data("Movement", "2024-11-20 12:00", 10) #filler code
    assert data.activity == "Movement", "Data activity should be Movement"#filler code
    print("Init Data was successful")
def test_protection_init():
    protection = Protection("Protected", "High", 80) #filler code
    assert protection.area == "Protected", "Area status should be Protected"#filler code
    print("Init Protection was successful")
def test_tourist_init():
    tourist = Tourist("High", "Heavy", "Eco-Tourism policies") #filler code
    assert tourist.impact_type == "High", "Tourist impact type should be High"#filler code
    print("Init Tourist was successful")

# Run our tests functions inside of an error handler


if __name__ == "__main__" :
        print ("Running tests...\n")
        try:
            test_tiger_init()
            test_habitat_init()
            test_poaching_init()
            test_prey_init()
            test_data_init()
            test_protection_init()
            test_tourist_init()
            #all tests functions here
            print ("\nAll tests passed! ✨")
        except AssertionError as e:
            print(f"\n❌ Test failed: {str(e)}")
