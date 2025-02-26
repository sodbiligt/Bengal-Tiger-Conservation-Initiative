import openai
openai.api_key = "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"
class Tiger:
    def __init__(self, name, average_weight, average_height, current_status, population):
        self.name = name
        self.weight = average_weight
        self.height= average_height
        self.status=current_status
        self.population=population
# other tiger attributes  
class Habitat:
    def __init__(self, location, temperature, biome, protection_status, population, human_activity):
        self.biome = biome
        self.location = location
        self.temperature = temperature
        self.protection_status = protection_status
        self.population = population
        self.human = human_activity
class Poaching:
    def __init__(self, date, method, victim):
        self.date=date
        self.method=method
        self.victim=victim
class Prey:
    def __init__(self, sci_name, prey_population):
        self.sci_name=sci_name
        self.prey_population=prey_population
class Data:
    def __init__(self, activity, time_stamp, population_flux):
        self.activity=activity
        self.time_stamp=time_stamp
        self.population_flux=population_flux #over 4 years
class Protection:
    def __init__(self, area_status, threat_level, updated_population):
        self.area=area_status
        self.threat=threat_level
        self.updated_population=updated_population
class Tourist: 
    def __init__(self, impact_type, tourism_level, policies):
        self.impact_type = impact_type
        self.tourism_level = tourism_level
        self.policies = policies
## tiger action
class TigerAction:
    def __init__(self, tiger_name):
        self.tiger_name = tiger_name
        self.actions = []  # List of actions performed on this tiger

    def input_name(self):
        # Placeholder for user input logic
        pass

    def add_action(self, action_name, timestamp):
        # Add a new action to the actions list
        self.actions.append({'action': action_name, 'timestamp': timestamp})

    def get_last_interaction(self):
        # Return the last action performed on the tiger
        if self.actions:
            return self.actions[-1]['action'] + " on " + self.actions[-1]['timestamp']
        return "No actions yet"
