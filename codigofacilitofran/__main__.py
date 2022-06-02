import logging

from codigofacilitofran import unreleased

logging.basicConfig(level=logging.INFO)

if __name__=='__main__':
    """
        INFO ->10
        DEBUG ->20
        WARNING ->30
        ERROR   ->40
        CRITICAL ->50

    """
    logging.debug("Estamos comenzando la ejecución del paquete")
    # workshops=unreleased()
    logging.debug(help(unreleased))
    logging.debug("Estamos finalizando la ejecución del paquete")