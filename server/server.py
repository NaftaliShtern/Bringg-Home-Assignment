from flask import Flask, Response
import gene_service, http_utils, server.config as config

app = Flask(__name__)

@app.route("/genes/find/<GEN>")
def user(GEN):
    ret_stat = gene_service.find(config.DATA_FILE_PATH, GEN)
    return Response(status=http_utils.get_status_code(gene_service, ret_stat))

def run():
    app.run()
