import matplotlib.pyplot as plt
import pylab
from flask import *
from config import *

latex_runner = Blueprint('latex_runner', __name__)

# Using the Blueprint made with a path
@latex_runner.route(LATEX_ROUTE, methods=['GET'])
def renderTeX():
    try:    
        text_input = request.args.get('text')
        transparent_input = request.args.get('transparent')
        text_color_input = request.args.get('text_color')
        try:
            if text_input is None:
                return jsonify(
                    error = 'tex input is not provided', 
                    error_id = 'ERROR_NO_TEXT_INPUT_TRY_BLOCK',
                    fix = 'Do not leave the text parameter empty'
                    )
        except Exception as e:
            return jsonify(
                error = str(e), 
                error_id = 'ERROR_TEXT_INPUT_TRY_BLOCK',
                fix = 'check your text input again'
                )

        try:
            text = f"${text_input}$"
            plt.rcParams['mathtext.fontset'] = 'cm'
            plt.rcParams['font.family'] = 'DejaVu Serif'
            fig = pylab.figure()
            
            if text_color_input is None:
                fig.text(0, 0, text,color = '#01abe1')
            if text_color_input is not None:
                fig.text(0, 0, text,color = f'#{text_color_input}')
                
            if transparent_input is None:  
                fig.savefig('../latex.png', bbox_inches='tight', dpi = 1000,pad_inches = 0.05,transparent = False)
            if transparent_input is 'true':  
                fig.savefig('../latex.png', bbox_inches='tight', dpi = 1000,pad_inches = 0.05,transparent = True)
            if transparent_input is 'false':  
                fig.savefig('../latex.png', bbox_inches='tight', dpi = 1000,pad_inches = 0.05,transparent = False)
            filename = '../latex.png'
            plt.close(fig)
            return send_file(filename)
        
        except Exception as e:
            return e
        
    except Exception as e:
        return e