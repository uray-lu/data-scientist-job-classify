
VENV = ./venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip



help: 
	@echo '-----------------------------------------------------------------------------------'
	@echo '|Use the following command line to reproduce the experiments and statistical tests|'
	@echo '-----------------------------------------------------------------------------------'



install: # make venv and install the packages needed.
install: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

data_manipulation: #combine raw data
data_manipulation: $(VENV)
	. venv/bin/activate;
	@python ./src/data_manipulation.py


feature_engineering: # Extract feature and modify the data
feature_engineering: $(VENV)
	. venv/bin/activate;
	@python ./src/Feature_Engineering.py




model_construct: # tuning/training/save model
model_construct: $(VENV)
	. venv/bin/activate;
	@python ./model/model.py


product_test: # Test the model output.
product_test: $(VENV)
	. venv/bin/activate;
	@python ./backend/product.py


app: # Show the web app.
app: $(VENV)
	. venv/bin/activate;
	@streamlit run streamlit_app.py


clean: #clean the venv and __pycache__
clean: 
	rm -rf __pycache__
	rm -rf $(VENV)



	