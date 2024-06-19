from flask import Flask, request, jsonify
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)


@app.route("/execute", methods=["POST"])
def execute_code():

    def max_continuous_gain_and_loss(symbol, period):
        try:
            stock_data = yf.download(symbol, period=period)

            stock_data["Pct Change"] = stock_data["Close"].pct_change()

            max_gain_days = 0
            max_loss_days = 0
            current_gain_days = 0
            current_loss_days = 0

            for pct_change in stock_data["Pct Change"]:
                if pct_change >= 0:
                    current_gain_days += 1
                    if current_gain_days > max_gain_days:
                        max_gain_days = current_gain_days
                    current_loss_days = 0
                elif pct_change < 0:
                    current_loss_days += 1
                    if current_loss_days > max_loss_days:
                        max_loss_days = current_loss_days
                    current_gain_days = 0

            return max_gain_days, max_loss_days
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {str(e)}")
            return None, None

    stocks = [
        "AARTIIND.NS",
        "ABB.NS",
        "ABBOTINDIA.NS",
        "ABCAPITAL.NS",
        "ABFRL.NS",
        "ACC.NS",
        "ADANIENT.NS",
        "ADANIPORTS.NS",
        "ALKEM.NS",
        "AMBUJACEM.NS",
        "APOLLOHOSP.NS",
        "APOLLOTYRE.NS",
        "ASHOKLEY.NS",
        "ASIANPAINT.NS",
        "ASTRAL.NS",
        "ATUL.NS",
        "AUBANK.NS",
        "AUROPHARMA.NS",
        "AXISBANK.NS",
        "BAJAJ-AUTO.NS",
        "BAJAJFINSV.NS",
        "BAJFINANCE.NS",
        "BALKRISIND.NS",
        "BALRAMCHIN.NS",
        "BANDHANBNK.NS",
        "BANKBARODA.NS",
        "BEL.NS",
        "BERGEPAINT.NS",
        "BHARATFORG.NS",
        "BHARTIARTL.NS",
        "BHEL.NS",
        "BIOCON.NS",
        "BOSCHLTD.NS",
        "BPCL.NS",
        "BRITANNIA.NS",
        "BSOFT.NS",
        "CANBK.NS",
        "CANFINHOME.NS",
        "CHAMBLFERT.NS",
        "CHOLAFIN.NS",
        "CIPLA.NS",
        "COALINDIA.NS",
        "COFORGE.NS",
        "COLPAL.NS",
        "CONCOR.NS",
        "COROMANDEL.NS",
        "CROMPTON.NS",
        "CUB.NS",
        "CUMMINSIND.NS",
        "DEEPAKNTR.NS",
        "DIVISLAB.NS",
        "DIXON.NS",
        "DLF.NS",
        "DRREDDY.NS",
        "EICHERMOT.NS",
        "ESCORTS.NS",
        "EXIDEIND.NS",
        "FEDERALBNK.NS",
        "GAIL.NS",
        "GLENMARK.NS",
        "GMRINFRA.NS",
        "GNFC.NS",
        "GODREJCP.NS",
        "GODREJPROP.NS",
        "GRANULES.NS",
        "GRASIM.NS",
        "GUJGASLTD.NS",
        "HAL.NS",
        "HAVELLS.NS",
        "HCLTECH.NS",
        "HDFCAMC.NS",
        "HDFCBANK.NS",
        "HDFCLIFE.NS",
        "HEROMOTOCO.NS",
        "HINDALCO.NS",
        "HINDCOPPER.NS",
        "HINDPETRO.NS",
        "HINDUNILVR.NS",
        "IBULHSGFIN.NS",
        "ICICIBANK.NS",
        "ICICIGI.NS",
        "ICICIPRULI.NS",
        "IDEA.NS",
        "IDFC.NS",
        "IDFCFIRSTB.NS",
        "IEX.NS",
        "IGL.NS",
        "INDHOTEL.NS",
        "INDIACEM.NS",
        "INDIAMART.NS",
        "INDIGO.NS",
        "INDUSINDBK.NS",
        "INDUSTOWER.NS",
        "INFY.NS",
        "IOC.NS",
        "IPCALAB.NS",
        "IRCTC.NS",
        "ITC.NS",
        "JINDALSTEL.NS",
        "JKCEMENT.NS",
        "JSWSTEEL.NS",
        "JUBLFOOD.NS",
        "KOTAKBANK.NS",
        "L&TFH.NS",
        "LALPATHLAB.NS",
        "LAURUSLABS.NS",
        "LICHSGFIN.NS",
        "LT.NS",
        "LTIM.NS",
        "LTTS.NS",
        "LUPIN.NS",
        "M&M.NS",
        "M&MFIN.NS",
        "MANAPPURAM.NS",
        "MARICO.NS",
        "MARUTI.NS",
        "MCDOWELL-N.NS",
        "MCX.NS",
        "METROPOLIS.NS",
        "MFSL.NS",
        "MGL.NS",
        "MOTHERSON.NS",
        "MPHASIS.NS",
        "MRF.NS",
        "MUTHOOTFIN.NS",
        "NATIONALUM.NS",
        "NAUKRI.NS",
        "NAVINFLUOR.NS",
        "NESTLEIND.NS",
        "NMDC.NS",
        "NTPC.NS",
        "OBEROIRLTY.NS",
        "OFSS.NS",
        "ONGC.NS",
        "PAGEIND.NS",
        "PEL.NS",
        "PERSISTENT.NS",
        "PETRONET.NS",
        "PFC.NS",
        "PIDILITIND.NS",
        "PIIND.NS",
        "PNB.NS",
        "POLYCAB.NS",
        "POWERGRID.NS",
        "PVRINOX.NS",
        "RAMCOCEM.NS",
        "RBLBANK.NS",
        "RECLTD.NS",
        "RELIANCE.NS",
        "SAIL.NS",
        "SBICARD.NS",
        "SBIN.NS",
        "SHREECEM.NS",
        "SHRIRAMFIN.NS",
        "SIEMENS.NS",
        "SRF.NS",
        "SUNPHARMA.NS",
        "SUNTV.NS",
        "SYNGENE.NS",
        "TATACHEM.NS",
        "TATACOMM.NS",
        "TATACONSUM.NS",
        "TATAMOTORS.NS",
        "TATAPOWER.NS",
        "TATASTEEL.NS",
        "TCS.NS",
        "TECHM.NS",
        "TITAN.NS",
        "TORNTPHARM.NS",
        "TRENT.NS",
        "TVSMOTOR.NS",
        "UBL.NS",
        "ULTRACEMCO.NS",
        "UPL.NS",
        "VEDL.NS",
        "VOLTAS.NS",
        "WIPRO.NS",
        "ZEEL.NS",
        "ZYDUSLIFE.NS",
    ]

    results = {}
    trailing_days = {}
    results_pct = {}
    trailing_pct = {}

    def max_current_gain(symbol, period_gain):
        try:
            stock_data = yf.download(symbol, period=period_gain)

            stock_data["Pct Change"] = stock_data["Close"].pct_change()

            max_gain_days = 0
            current_gain_days = 0

            for pct_change in stock_data["Pct Change"]:
                if pct_change >= 0:
                    current_gain_days += 1
                    if current_gain_days >= max_gain_days:
                        max_gain_days = current_gain_days
                else:
                    current_gain_days = 0

            if stock_data["Pct Change"].iloc[-1] >= 0:
                current_gain_days += 1
                if current_gain_days >= max_gain_days:
                    max_gain_days = current_gain_days

            return max_gain_days
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {str(e)}")
            return None

    def max_current_loss(symbol, period_loss):
        try:
            stock_data = yf.download(symbol, period=period_loss)

            stock_data["Pct Change"] = stock_data["Close"].pct_change()

            max_loss_days = 0
            current_loss_days = 0

            for pct_change in stock_data["Pct Change"]:
                if pct_change < 0:
                    current_loss_days += 1
                    if current_loss_days >= max_loss_days:
                        max_loss_days = current_loss_days
                else:
                    current_loss_days = 0

            if stock_data["Pct Change"].iloc[-1] < 0:
                current_loss_days += 1
                if current_loss_days >= max_loss_days:
                    max_loss_days = current_loss_days

            return max_loss_days
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {str(e)}")
            return None

    def max_pct_gain_and_loss(symbol, period):
        try:
            stock_data = yf.download(symbol, period=period)

            stock_data["Pct Change"] = stock_data["Close"].pct_change()

            max_gain_pct = 0
            max_loss_pct = 0
            current_gain_pct = 0
            current_loss_pct = 0

            for pct_change in stock_data["Pct Change"]:
                if pct_change >= 0:
                    current_gain_pct += pct_change
                    if current_gain_pct >= max_gain_pct:
                        max_gain_pct = current_gain_pct
                    current_loss_pct = 0
                elif pct_change < 0:
                    current_loss_pct += pct_change
                    if abs(current_loss_pct) >= abs(max_loss_pct):
                        max_loss_pct = current_loss_pct
                    current_gain_pct = 0

            return max_gain_pct, max_loss_pct
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {str(e)}")
            return None, None

    def max_pct_gain(symbol, period):
        try:
            stock_data = yf.download(symbol, period=period)

            stock_data["Pct Change"] = stock_data["Close"].pct_change()

            max_gain_pct = 0
            current_gain_pct = 0

            for pct_change in stock_data["Pct Change"]:
                if pct_change >= 0:
                    current_gain_pct += pct_change
                    if current_gain_pct >= max_gain_pct:
                        max_gain_pct = current_gain_pct
                elif pct_change < 0:
                    current_gain_pct = 0

            return max_gain_pct
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {str(e)}")
            return None

    def max_pct_loss(symbol, period):
        try:
            stock_data = yf.download(symbol, period=period)

            stock_data["Pct Change"] = stock_data["Close"].pct_change()

            max_loss_pct = 0
            current_loss_pct = 0

            for pct_change in stock_data["Pct Change"]:
                if pct_change >= 0:
                    current_loss_pct = 0
                elif pct_change < 0:
                    current_loss_pct += pct_change
                    if abs(current_loss_pct) >= abs(max_loss_pct):
                        max_loss_pct = current_loss_pct

            return max_loss_pct
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {str(e)}")
            return None

    for symbol in stocks:
        max_gain_days, max_loss_days = max_continuous_gain_and_loss(symbol, "252d")
        if max_gain_days is not None and max_loss_days is not None:
            results[symbol] = {
                "Max Gain Days": max_gain_days,
                "Max Loss Days": max_loss_days,
            }
        else:
            results[symbol] = {"Error": "Failed to fetch data due to timeout"}

    for symbol in stocks:
        max_gain_pct, max_loss_pct = max_pct_gain_and_loss(symbol, "252d")
        if max_gain_pct is not None and max_loss_pct is not None:
            results_pct[symbol] = {
                "Max pct Gain": max_gain_pct,
                "Max pct Loss": max_loss_pct,
            }
        else:
            results[symbol] = {"Error": "Failed to fetch data due to timeout"}

    for symbol, data in results.items():
        current_gain_days = max_current_gain(symbol, str(data["Max Gain Days"]) + "d")
        current_loss_days = max_current_loss(symbol, str(data["Max Loss Days"]) + "d")
        if current_gain_days is not None and current_loss_days is not None:
            trailing_days[symbol] = {
                "Current Gain Days": current_gain_days,
                "Current Loss Days": current_loss_days,
            }

    for symbol, data in results.items():
        trailing_gain_pct = max_pct_gain(symbol, str(data["Max Gain Days"] + 1) + "d")
        trailing_loss_pct = max_pct_loss(symbol, str(data["Max Loss Days"] + 1) + "d")
        if trailing_gain_pct is not None and trailing_loss_pct is not None:
            trailing_pct[symbol] = {
                "Trailing Gain pct": trailing_gain_pct,
                "Trailing Loss pct": trailing_loss_pct,
            }

    results1 = {}
    results2 = {}
    results3 = {}
    results4 = {}

    for symbol, data in results.items():
        if data["Max Loss Days"] == trailing_days[symbol]["Current Loss Days"]:
            results1[symbol] = {
                "Trailing Loss Days": trailing_days[symbol]["Current Loss Days"],
                "Max Loss Days": data["Max Loss Days"],
            }

    if not results1:
        result1 = {"error": "No stock(s) match the criterion for maximum loss days"}
    else:
        result1 = results1

    for symbol, data in results.items():
        if data["Max Gain Days"] == trailing_days[symbol]["Current Gain Days"]:
            results2[symbol] = {
                "Trailing Gain Days": trailing_days[symbol]["Current Gain Days"],
                "Max Gain Days": data["Max Gain Days"],
            }

    if not results2:
        result2 = {"error": "No stock(s) match the criterion for maximum gain days"}
    else:
        result2 = results2

    for symbol, data in results.items():
        if symbol in results_pct and symbol in trailing_pct:
            max_gain_pct = results_pct[symbol].get("Max pct Gain", None)
            trailing_gain_pct_val = trailing_pct[symbol].get("Trailing Gain pct", None)

        if max_gain_pct is not None and trailing_gain_pct_val is not None:
            if abs(max_gain_pct - trailing_gain_pct_val) <= 0.015:
                results3[symbol] = {
                    "Trailing Gain pct": trailing_gain_pct_val,
                    "Max Gain pct": max_gain_pct,
                }

    if not results3:
        results3 = {"error": "No stock(s) match the criterion for maximum gain days"}
    else:
        results3 = results3

    for symbol, data in results.items():
        if symbol in results_pct and symbol in trailing_pct:
            max_loss_pct = results_pct[symbol].get("Max pct Loss", None)
            trailing_loss_pct_val = trailing_pct[symbol].get("Trailing Loss pct", None)

        if max_loss_pct is not None and trailing_loss_pct_val is not None:
            if abs(max_loss_pct - trailing_loss_pct_val) <= 0.015:
                results4[symbol] = {
                    "Trailing Loss pct": trailing_loss_pct_val,
                    "Max Loss pct": max_loss_pct,
                }

    if not results4:
        results4 = {"error": "No stock(s) match the criterion for maximum gain days"}
    else:
        results4 = results4

    return jsonify(
        {
            "max_loss_days": result1,
            "max_gain_days": result2,
            "gain_pct_change": results3,
            "loss_pct_change": results4,
        }
    )


if __name__ == "__main__":
    app.run(debug=True, port=8000)
