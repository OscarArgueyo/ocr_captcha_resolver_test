## OCR Captcha Resolver (test) With Pytesseract and Selenium


Instructions
--------------------------------------------------------------------------------
1. Run `pip install -r requirements.txt` to install dependencies
2. Run `python -m http.server --directory target_web` to start the dummy site with captcha
3. Navigate to http://localhost:8000 in your browser and check de site. Try few captchas and see the results
4. Run `python app/cli.py [--iterations number]` and check app/results.txt to check when the captcha solver was successful.

