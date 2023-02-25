"""
Author:Renan
Data: 02/08/2023
_
"""
import sys
import logging
import argparse
from main import Translate
from rich.console import Console


class Program:
    VERSION = "1.2.0"

    def __init__(self):
        # Make in the constructor the variable available and
        # usable to all class and your methods
        self.__args = sys.argv
        self.__commands = ['-print', '-file', '-trans']
        self.__translate = Translate()
        self.c = Console()
        self.__run()
        
    def __run(self):
        self.parser = argparse.ArgumentParser(
            prog="auto-sub",
            description="Auto translate files for sub",
            epilog="Renan "
        )
        self.parser.add_argument("translate",type= str,help="Provides the file path here")
        self.arg_parse = self.parser.parse_args()

        if self.arg_parse.translate:
            self.read_file()

        return None
  
    # Excluir essa função
    def translate(self, text: str, *argv) -> str:
        if (text == null): 
            return
        print(f"text: {text}")
        return text
        pass

    def read_file(self):
        if self.arg_parse.translate:
            self.c.log(f"PATH OF THE FILE  [yellow]{self.arg_parse.translate}")
            with open(self.arg_parse.translate, encoding="UTF-8") as file:
                self.c.log(f"[green]Content of the file {file.readlines()}")
                content = file.readlines()
                self.__translate.translate(content)
                # always close on finish
                file.close()


        if self.find_arg('-file') is True:
            print("file!")
            pass

        pass

    # This method find the spefics commands for the command line
    # like -p -file -translate -print
    # return None
    def find_arg(self, command: str) -> bool:
        for co in self.__commands:
            if co == command:
                print('command founded')
                return True
            else:
                return False
            print(co)
                   
        return False
    

if __name__ == '__main__':
    auto_sub = Program()