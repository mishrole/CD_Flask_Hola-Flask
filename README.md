Pasos para correr el proyecto
===

1. pip install pipenv
2. pipenv install flask
3. pipenv shell
4. python server.py

Ubuntu WS2L
===

1. Instalar pipenv por usuario o global
   - python -m pip install --user pipenv
   - pip3 install pipenv
2. Instalar Flask (por carpeta de proyecto) 
    - pipenv install flask
3. Exportar path
    - echo 'export PATH="${HOME}/.local/bin:$PATH"' >> ~/.bashrc
4. Crear environment (tarda regular en crear, sólo espera)
    - pipenv shell
5. Correr proyecto
    - python server.py