import subprocess 
from segregate_repo import Segregator
import os, sys

class PushCode:
    def __init__(self):
        self.directory = {'home_dir': sys.path[0]}
    
    def segregate_repo(self):
        segregator = Segregator()
        segregator.CreateFolders()
        segregator.MoveFilesToFolders()    
    
    def push_commands(self):
        os.chdir(self.directory['home_dir'])
        commit_msg = sys.argv[1] if len(sys.argv)>1 else 'Minor'
        branch_name = sys.argv[2] if len(sys.argv)>2 else 'master'
        push_success = False
        try:
            add_cmd = subprocess.run(["git", "add", "."], capture_output = True)
            commit_cmd = subprocess.run(["git", "commit", "-m", commit_msg], capture_output = True)
            push_cmd = subprocess.run(["git", "push", "origin", branch_name], capture_output = True)
            push_success = push_cmd.returncode == 0
        except:
            print("\n\t######\tPush failed! Error occured while pushing...\t######\n")
        
        
        if push_success:
            print("\t-> Push successful")
        else:
            print(push_cmd.returncode)
            print("\t -> Push failed")
    
if __name__ == '__main__': # Specify message and branch name has CMD arguments
    push_obj = PushCode()
    push_obj.segregate_repo() 
    push_obj.push_commands()
