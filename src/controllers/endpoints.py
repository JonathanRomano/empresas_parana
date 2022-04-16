from flask import Flask
from flask_restplus import Api, Resource
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

from src.server.instance import server

app, api = server.app, server.api

@api.route('/empresaFacil')
class Empresa_facil(Resource):
    def post(self):
        x = api.payload

        return x

    def get(self):
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

        driver.get('https://uptogether.vercel.app/')

        texto = driver.find_element_by_xpath('/html/body/div/div/main/div[1]/div[1]/div[1]/h1').text

        driver.close()
        
        teste = "Up together"

        return teste
