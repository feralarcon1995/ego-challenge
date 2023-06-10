from vehicles.models import Cars

def create_default_cars():
    default_cars = [
        {
            'brand': 'Toyota',
            'model': 'GR Corolla 2023',
            'category': 'car',
            'img':'/cars/grcorolla.png',
            'title':'Sedán deportivo de alto rendimiento con estilo agresivo y potencia emocionante',
            'description':'Sapien porttitor varius feugiat habitant potenti proin nibh sagittis, nostra cum nisi egestas tortor hendrerit torquent lacus in, venenatis eros pulvinar volutpat faucibus dui laoreet. Habitasse per turpis ultricies himenaeos dapibus nunc ornare risus, mauris leo curabitur praesent varius quam nec ridiculus suscipit, quisque vehicula consequat metus cubilia vel potenti. Sociis eleifend in eu faucibus sodales fusce interdum ut odio sapien, lobortis justo magna mollis habitant imperdiet cum penatibus aptent, vestibulum felis tortor conubia rhoncus pulvinar dis facilisi neque.',
            'year': 2022,
            'price': 2683500
        },
        {
            'brand': 'Toyota',
            'model': 'Corolla Hatchback 2023',
            'category': 'car',
            'img':'/cars/hatchback2023.webp',
            'title':'El Corolla Hatchback 2023 está listo para la carretera con su estilo deportivo, tecnología intuitiva y una respuesta de manejo emocionante.',
            'description':'Sapien porttitor varius feugiat habitant potenti proin nibh sagittis, nostra cum nisi egestas tortor hendrerit torquent lacus in, venenatis eros pulvinar volutpat faucibus dui laoreet. Habitasse per turpis ultricies himenaeos dapibus nunc ornare risus, mauris leo curabitur praesent varius quam nec ridiculus suscipit, quisque vehicula consequat metus cubilia vel potenti. Sociis eleifend in eu faucibus sodales fusce interdum ut odio sapien, lobortis justo magna mollis habitant imperdiet cum penatibus aptent, vestibulum felis tortor conubia rhoncus pulvinar dis facilisi neque.',
            'year': 2023,
            'price': 2983000
        },
        {
            'brand': 'Toyota',
            'model': 'Tacoma',
            'category': 'pickup',
            'img':'/cars/tacoma.png',
            'title':'Diseñada para aventuras memorables',
            'description':'Sapien porttitor varius feugiat habitant potenti proin nibh sagittis, nostra cum nisi egestas tortor hendrerit torquent lacus in, venenatis eros pulvinar volutpat faucibus dui laoreet. Habitasse per turpis ultricies himenaeos dapibus nunc ornare risus, mauris leo curabitur praesent varius quam nec ridiculus suscipit, quisque vehicula consequat metus cubilia vel potenti. Sociis eleifend in eu faucibus sodales fusce interdum ut odio sapien, lobortis justo magna mollis habitant imperdiet cum penatibus aptent, vestibulum felis tortor conubia rhoncus pulvinar dis facilisi neque.',
            'year': 2023,
            'price': 1983050
        },
        {
            'brand': 'Toyota',
            'model': 'Tundra',
            'category': 'pickup',
            'img':'/cars/tundra.png',
            'title':'Diseñada para aventuras memorables',
            'description':'Sapien porttitor varius feugiat habitant potenti proin nibh sagittis, nostra cum nisi egestas tortor hendrerit torquent lacus in, venenatis eros pulvinar volutpat faucibus dui laoreet. Habitasse per turpis ultricies himenaeos dapibus nunc ornare risus, mauris leo curabitur praesent varius quam nec ridiculus suscipit, quisque vehicula consequat metus cubilia vel potenti. Sociis eleifend in eu faucibus sodales fusce interdum ut odio sapien, lobortis justo magna mollis habitant imperdiet cum penatibus aptent, vestibulum felis tortor conubia rhoncus pulvinar dis facilisi neque.',
            'year': 2022,
            'price': 1963007
        },
        {
            'brand': 'Toyota',
            'model': 'Hilux',
            'category': 'pickup',
            'img':'/cars/hilux.webp',
            'title':'Una nueva era en Pickups, gracias a su eficiencia y capacidad de adaptación a todo tipo de climas, terrenos y usos, en ciudad, carretera e incluso terracería el Toyota Hilux es la solución perfecta a todas tus necesidades.',
            'description':'Sapien porttitor varius feugiat habitant potenti proin nibh sagittis, nostra cum nisi egestas tortor hendrerit torquent lacus in, venenatis eros pulvinar volutpat faucibus dui laoreet. Habitasse per turpis ultricies himenaeos dapibus nunc ornare risus, mauris leo curabitur praesent varius quam nec ridiculus suscipit, quisque vehicula consequat metus cubilia vel potenti. Sociis eleifend in eu faucibus sodales fusce interdum ut odio sapien, lobortis justo magna mollis habitant imperdiet cum penatibus aptent, vestibulum felis tortor conubia rhoncus pulvinar dis facilisi neque.',
            'year': 2021,
            'price': 3353000
        },
        {
            'brand': 'Toyota',
            'model': 'Corolla Cross',
            'category': 'suv',
            'img':'/cars/hilux.webp',
            'title':'Crossover compacto con estilo moderno y versatilidad urbana',
            'description':'Sapien porttitor varius feugiat habitant potenti proin nibh sagittis, nostra cum nisi egestas tortor hendrerit torquent lacus in, venenatis eros pulvinar volutpat faucibus dui laoreet. Habitasse per turpis ultricies himenaeos dapibus nunc ornare risus, mauris leo curabitur praesent varius quam nec ridiculus suscipit, quisque vehicula consequat metus cubilia vel potenti. Sociis eleifend in eu faucibus sodales fusce interdum ut odio sapien, lobortis justo magna mollis habitant imperdiet cum penatibus aptent, vestibulum felis tortor conubia rhoncus pulvinar dis facilisi neque.',
            'year': 2020,
            'price': 3353000
        },
        {
            'brand': 'Toyota',
            'model': '4Runner',
            'category': 'suv',
            'img':'/cars/4runner.webp',
            'title':'Potente SUV con capacidad todoterreno y comodidad para la familia',
            'description':'Sapien porttitor varius feugiat habitant potenti proin nibh sagittis, nostra cum nisi egestas tortor hendrerit torquent lacus in, venenatis eros pulvinar volutpat faucibus dui laoreet. Habitasse per turpis ultricies himenaeos dapibus nunc ornare risus, mauris leo curabitur praesent varius quam nec ridiculus suscipit, quisque vehicula consequat metus cubilia vel potenti. Sociis eleifend in eu faucibus sodales fusce interdum ut odio sapien, lobortis justo magna mollis habitant imperdiet cum penatibus aptent, vestibulum felis tortor conubia rhoncus pulvinar dis facilisi neque.',
            'year': 2021,
            'price': 1439000
        },
    ]

    for car_data in default_cars:
        Cars.objects.create(**car_data)

    print('autos creados')   

