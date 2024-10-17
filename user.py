from diary import Diary

class User :
    def __init__(self, name ):
        self.name = name
        self.entries = []

    def add_entry( self, doj ):
        self.entries.append(doj)
        print("Successfully added.........")

    def show_entries( self ) :
        print("--------------------------------------------")
        print("---------------- View Entries -------------")
        print(f"Id\tcontent\tDate")
        for i in self.entries :
            print(f"{i.title}\t{i.content}\t{i.date}")
        print("--------------------------------------------")
            
    def delete_entry( self, name ) :
        self.entries.pop(name)
        print("Deleted")