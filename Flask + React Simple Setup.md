---
id: 20250306174518
creation_date: 2025-03-06
aliases: 
tags:
---
1. In Frontend: `npm run build` 
	- Vite: New Folder `dist` is created
	- CRA: New Folder `build` is created
2. Create `static` folder in backend
3. Copy contents from `build`/`dist` folder to `static` folder
4. In `backend.py` 
	1. Change this line `app = Flask(__name__, template_folder='dist', static_url_path="/") # Create a Flask app`
	2. Add 
	   ```python
		@app.route('/', methods=['GET'])
		def home():
		print(app.static_folder, "index.html")
		# return index.html
		return send_from_directory(app.static_folder, "index.html")
		
		# Handle React Router Paths
		@app.route("/<path:path>")
		def serve_static_files(path):
		try:
		print(path)
		return send_from_directory(app.static_folder, path)
		except:
		return send_from_directory(app.static_folder, "index.html") # Serve React for unknown pathsç
		```