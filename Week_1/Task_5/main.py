

from entities import Player, NPC, Object


vr_world = []

def simulate_interaction(entities_list):
    
    if not entities_list:
        print("No entities found in the VR world.")
        return

    print("\n--- Commencing VR Interactions ---")
    for entity in entities_list:
        entity.interact()
    print("----------------------------------")

while True:
    print("\n--- VR Simulation Menu ---")
    print("1 - Add Entity")
    print("2 - Interact with Entities")
    print("3 - Exit")

    choice = input("Select an option: ")

    try:
        if choice == '1':
            
            print("\nSelect Entity Type: 1-Player, 2-NPC, 3-Object")
            ent_type = input("Choice: ")
            
            ent_name = input("Enter entity name: ")
            ent_pos = input("Enter position (e.g., 10x, 20y): ")

            if ent_type == '1':
                hp = int(input("Enter player health (e.g., 100): "))
                vr_world.append(Player(name=ent_name, position=ent_pos, health=hp))
                print(f"Player '{ent_name}' added to the simulation.")
            
            elif ent_type == '2':
                npc_role = input("Enter NPC role (e.g., Merchant, Guard): ")
                vr_world.append(NPC(name=ent_name, position=ent_pos, role=npc_role))
                print(f"NPC '{ent_name}' added to the simulation.")
            
            elif ent_type == '3':
                obj_kind = input("Enter object type (e.g., Tree, Rock, Door): ")
                vr_world.append(Object(name=ent_name, position=ent_pos, object_type=obj_kind))
                print(f"Object '{ent_name}' added to the simulation.")
            
            else:
                
                print("Invalid entity type selected.")

        elif choice == '2':
            
            simulate_interaction(vr_world)

        elif choice == '3':
            
            print("Exiting VR Simulation. Goodbye!")
            break
        
        else:
            
            print("Invalid menu choice. Please try again.")

    except ValueError:
        
        print("Error: Invalid input format. Please enter correct data types.")
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")
