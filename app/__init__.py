import mpld3
from flask import Flask
from flask import render_template, request, redirect, url_for
from plotting import draw_fig
import matplotlib.pyplot as plt
import numpy as np

app = Flask(__name__)
app.config.from_object('config')


class OptionPosition(object):
    def __init__(self, side, quantity, instrument, strike, dte, vol, price):
        self.side = side
        self.quantity = quantity
        self.instrument = instrument
        self.strike = strike
        self.dte = dte
        self.vol = vol
        self.price = price

    def calculate_payoff(self, prices):
        if self.instrument== 'call':
            payoff = map(lambda x: max(x-self.strike, 0), prices)
        else:
            payoff = map(lambda x: max(self.strike-x, 0), prices)

        return payoff

    def to_string(self):
        return '{} {} x {} {}'.format(self.side.capitalize(), self.quantity, self.strike, self.instrument.capitalize())

plot_to_render = None

@app.route('/')
def home():
    return render_template('options.html', plot=plot_to_render)



@app.route('/query', methods=['POST'])
def query():
    global plot_to_render, rendered_positions

    min_strike = 1000
    max_strike = 0

    i = 1
    options_positions = []
    while True:
        try:
            side = request.form['side'+str(i)]
            quantity = float(request.form['quantity'+str(i)])
            instrument = request.form['instrument'+str(i)]
            strike = float(request.form['strike'+str(i)])
            min_strike = min(strike, min_strike)
            max_strike = max(strike, max_strike)
            dte = float(request.form['dte'+str(i)])
            vol = float(request.form['vol'+str(i)])
            price = float(request.form['price'+str(i)])
            options_positions.append(OptionPosition(side, quantity, instrument, strike, dte, vol, price))
            i += 1
        except KeyError:
            break

    prices = np.linspace(max(0, min_strike-20), max_strike+20, num=100)
    payoffs = []
    position_strings = []
    for option_position in options_positions:
        payoffs.append(option_position.calculate_payoff(prices))
        position_strings.append(option_position.to_string())

    payoff = [sum(x) for x in zip(*payoffs)]

    fig, ax = plt.subplots()
    fig.suptitle('P/L', fontsize=20)
    ax.plot(prices, payoff)
    ax.set_xlabel('Option position value ($)')
    ax.set_ylabel('Underlying price at expiration ($)')

    extra = plt.Rectangle((0, 0), 1, 1, fc="w", fill=False, edgecolor='none', linewidth=0)
    ax.legend([extra]*len(position_strings), tuple([position_strings]))

    plot_to_render = mpld3.fig_to_html(fig)
    rendered_positions = position_strings

    return redirect(url_for('home', positions=position_strings))