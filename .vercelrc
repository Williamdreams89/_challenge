{
  "builds": [
    {
      "src": "build_files.sh",
      "use": "@vercel/build-script",
      "config": {
        "commands": [
          "python -m venv venv",  
          "source venv/bin/activate",  
          "pip install -r requirements.txt"  
        ]
      }
    }
  ],
  "functions": { "prebuild": "build_files.sh" }  
}
