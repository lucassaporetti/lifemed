from lifemed_api.app import LifemedAPI  # pragma: no cover
from lifemed_api.components.utils.arg_parser import ArgParse  # pragma: no cover

if __name__ == "__main__":  # pragma: no cover
    args = ArgParse().set_parser()  # pragma: no cover
    LifemedAPI.run(args)  # pragma: no cover
