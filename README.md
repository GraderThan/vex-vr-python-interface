# Vex VR Python Interface for IDEs

👋 Welcome, Python enthusiasts and Vex Robotics aficionados! Introducing our Python interface specifically crafted for Vex VR. This interface transcends a regular library, aiming to enhance your coding journey with intelligent type hints, syntax error checks, and auto-complete functionalities in your IDE.

## Why This Repository?
Wondering about the necessity of this repository? Here are the compelling reasons:

1. **Type-Hinting, Syntax Error Checking & Auto-Completion**: Whether you're using the Grader Than IDE, Visual Studio Code, or PyCharm, this interface is designed to assist your IDE in offering smart hints, syntax error checking, and suggestions as you code. This not only minimizes errors but also accelerates your coding process.

2. **Leveraging IDE Features**: By utilizing this interface, you can fully exploit the power of your IDE, making coding in Vex VR more efficient and enjoyable.

3. **Temporary Solution**: View this as an interim fix. While we await Vex's official Python package release, this interface serves as a reliable stand-in, ensuring you're not left in the lurch. 

## Getting Started With Grader Than:

Follow these steps to enable your students to have full IDE support for Vex VR.

**Prerequisites:** A [Grader Than Workspace setup](https://docs.graderthan.com/workspace/create/) is required.

1. Create a `vex vr` dependency. Refer to these [instructions](https://docs.graderthan.com/workspace/config/#create-a-dependency) for guidance on setting up a dependency.
2. Use the following script as your install guide for the `vex vr` dependency you just created:
   
```shell
#!/bin/bash

url=git+https://github.com/graderthan/vex-vr-python-interface.git

# Installing type-hinting and autocomplete tools
user_pip_path="/home/developer/Documents/code/.venv/bin/pip"
if [ -f "$user_pip_path" ]; then
   source "/home/developer/Documents/code/.venv/bin/activate"
   "$user_pip_path" install "$url"
   deactivate
else
   pip install "$url"
fi

# Configuration pyright to handle weird vex syntax issues
config_file="/home/developer/Documents/code/pyrightconfig.json"
config_content='{
  "reportUnusedCoroutine": "none",
  "reportWildcardImportFromLibrary": "none"
}'
echo "$config_content" > "$config_file"
```

3. **🥳 Completion!** Your students and course now have full IDE support for Vex VR.

## Contribution & Feedback
Your input and collaboration are vital for this community's growth. We encourage you to fork, submit pull requests, or open issues. Together, let's create the ultimate interim solution for Vex VR Python programmers!

## Acknowledgements
A heartfelt thanks to the Python and Vex robotics communities for their inspiration and enthusiasm. We're all eagerly anticipating the official Vex Python package – hopefully, it's on the horizon!