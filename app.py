#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora():
    resultado = None
    if request.method == 'POST':
        a = float(request.form['a'])
        b = float(request.form['b'])
        operacao = request.form['operacao']

        if operacao == 'soma':
            resultado = a + b
        elif operacao == 'subtracao':
            resultado = a - b
        elif operacao == 'multiplicacao':
            resultado = a * b
        elif operacao == 'divisao':
            if b == 0:
                resultado = 'Erro: Divisão por zero!'
            else:
                resultado = a / b

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
