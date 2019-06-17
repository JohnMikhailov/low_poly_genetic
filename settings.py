IMAGE_PATH = {

    'input': 'input.jpg',
    'output': 'output.jpg'
}

GENETIC_ALGORITHM_SETTINGS = {

    'gens_amount': 500,
    'threshold': (0.2, 0.5),
    'fitness': 0.5,
    'radius': 2,

    'start_method': {

        'generations': 15,
        'use_fitness': True
    }
}

CANNY = {

    'lower': 100,
    'upper': 200
}

settings = [GENETIC_ALGORITHM_SETTINGS, CANNY, IMAGE_PATH]
