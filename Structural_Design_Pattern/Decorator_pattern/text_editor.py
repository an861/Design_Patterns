"""
Text Editor - Decorator Design Pattern Problem Statement

Problem Statement:
Design a text editor component that allows users to apply multiple formatting options to a block of text
(e.g., bold, italic, underline, highlight, strikethrough). The formatting options should be flexible, composable,
and dynamically attachable at runtime without modifying the original text class.

Objectives:
    Build a core Text class that holds the original plain text.
    Provide the ability to decorate the text with one or more formatting styles.
    Users should be able to apply formatting like:
        Bold
        Italic
        Strikethrough
        <u>Underline</u>
Highlight
The system should preserve the base functionality of the text but allow additional behaviors (rendering styles)
to be added dynamically.
"""

from abc import ABC, abstractmethod
from typing import final

class TextEditor(ABC):

    @abstractmethod
    def get_description(self)->str:
        pass

    @abstractmethod
    def get_final_text(self)->str:
        pass

@final
class TextBase(TextEditor):

    def __init__(self, base_text: str):
        self.text = base_text

    def get_description(self):
        return "Text: {}".format(self.text)

    def get_final_text(self):
        return self.text
    
class TextFormatter(TextEditor):

    def __init__(self, text_editor: TextEditor):
        self._text_editor = text_editor

    
class BoldFormat(TextFormatter):

    def get_description(self):
        return self._text_editor.get_description() + " with Bold format"

    def get_final_text(self):
        return "\033[1m" + self._text_editor.get_final_text() + "\033[0m"
    
class ItalicFormat(TextFormatter):

    def get_description(self):
        return self._text_editor.get_description() + " with Italic format"

    def get_final_text(self):
        return "\033[3m" + self._text_editor.get_final_text() + "\033[0m"
    
class StrikethroughFormat(TextFormatter):

    def get_description(self):
        return self._text_editor.get_description() + " with Strikethrough format"

    def get_final_text(self):
        base =  self._text_editor.get_final_text()
        return ''.join([c + '\u0336' for c in base])
    


# CLI for the text formatter

def get_text():
    text = input("Enter the text to format: \n")
    return TextBase(text)


def get_formatted_text(final_text: object):
    print("\n Kindly choose from below formatting options:")
    format_options = {
        "1": BoldFormat,
        "2": ItalicFormat,
        "3": StrikethroughFormat
    }
    for k, v in format_options.items():
        print(f"{k}.{v.__name__}")
    formatted_text = input("\n Please select your preferred text formatters(eg: 1,2): \n").strip().split(",")
    for ft in formatted_text:
        formatter = format_options.get(ft.strip())
        if formatter:
            final_text = formatter(final_text)
    return final_text




def main():
    text = get_text()
    formatted_text = get_formatted_text(text)
    print("\n Here's the formatted text summary: \n")
    print("Description: {}".format(formatted_text.get_description()))
    print("Final text: {}".format(formatted_text.get_final_text()))

if __name__ == "__main__":
    main()


# STRIKE THROUGH
"""
Enter the text to format: 
hello

 Kindly choose from below formatting options:
1.BoldFormat
2.ItalicFormat
3.StrikethroughFormat

 Please select your preferred text formatters(eg: 1,2): 
3

 Here's the formatted text summary: 

Description: Text: hello with Strikethrough format
Final text: h̶e̶l̶l̶o̶
"""

# bold
"""
Enter the text to format: 
Ankita

 Kindly choose from below formatting options:
1.BoldFormat
2.ItalicFormat
3.StrikethroughFormat

 Please select your preferred text formatters(eg: 1,2): 
1

 Here's the formatted text summary: 

Description: Text: Ankita with Bold format
Final text: Ankita
"""

# italics
"""
Enter the text to format: 
live long

 Kindly choose from below formatting options:
1.BoldFormat
2.ItalicFormat
3.StrikethroughFormat

 Please select your preferred text formatters(eg: 1,2): 
2

 Here's the formatted text summary: 

Description: Text: live long with Italic format
Final text: live long
"""