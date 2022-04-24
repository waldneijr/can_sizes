import math
pi = math.pi

def main():
    name = '#1 picnic'
    radius = 6.83
    height = 10.16
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')

    name = '#1 Tall'
    radius = 7.78
    height = 11.91
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')




    name = '#2'
    radius = 8.73
    height = 11.59
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)   
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')



    name = '#2.5'
    radius = 10.32
    height = 11.91
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '#3 Cylinder'
    radius = 10.79
    height = 17.78
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '#5'
    radius = 13.02
    height = 14.29
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '6Z'
    radius = 5.40
    height = 8.89
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '8Z short'
    radius = 6.83
    height = 7.62
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '#10'
    radius = 15.72
    height = 17.78
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '#211'
    radius = 6.83
    height = 12.38
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '#300'
    radius = 7.82
    height = 11.27
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')


    name = '#303'
    radius = 8.10
    height = 11.11
    surface_area = calculate_surface_area(radius, height)
    volume = calculate_volume (radius, height)
    storage_efficience = volume / surface_area
    print(f'{name} - {storage_efficience:.1f}')

def calculate_surface_area(radius, height):
    surface_area = 2 * pi * radius * (radius + height)
    return surface_area

def calculate_volume(radius, height):
    volume = pi * (radius ** 2) * height
    return volume

def compute_storage_efficiency(radius, height):
    volume = calculate_volume(radius, height)
    surface_area = calculate_surface_area(radius, height)
    storage_efficiency = volume / surface_area 
    return storage_efficiency

main()


