from flask import Flask, request
import os
import lxml.etree

app = Flask(__name__)

# 🔴 Showcase: Secrets Detection
# FrogBot will detect this hardcoded dummy token
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

@app.route('/ping')
def ping():
    # 🔴 Showcase: SAST (Command Injection)
    # FrogBot SAST will catch the unsanitized user input passed directly to the OS
    target = request.args.get("ip", "127.0.0.1")
    os.system(f"ping -c 1 {target}")
    return "Ping executed!"

@app.route('/parse')
def parse_xml():
    # 🔴 Showcase: Contextual Analysis
    # FrogBot knows lxml is vulnerable (SCA), but because we are actively
    # calling the vulnerable function here, Contextual Analysis will flag this
    # as a highly exploitable, applicable CVE.
    xml_data = request.args.get("xml", "<root></root>")
    root = lxml.etree.fromstring(xml_data)
    return "Parsed!"

if __name__ == '__main__':
    app.run(debug=True)
