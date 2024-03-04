from django.http import JsonResponse
import re

# TODO update README.md

def format_uk_postcode(request):
    if request.method == 'GET':
        postcode = request.GET.get('postcode', None)
        if postcode:
            postcode = ''.join(character for character in postcode if character.isalnum())  
            postcode = f'{postcode[:-3]} {postcode[-3:]}'
            return JsonResponse({'formatted_postcode': f'{postcode.upper()}'})
        else:
            return JsonResponse({'error': 'No postcode provided'})
    else:
        return JsonResponse({'error': 'Only GET method is allowed'})

def validate_uk_postcode(request):
    if request.method == 'GET':
        postcode = request.GET.get('postcode', None)
        if postcode:
            # regex taken from https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting
            regex = r'^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$'
            
            if re.match(regex, postcode, re.IGNORECASE):
                return JsonResponse({'postcode': f'{postcode}', 'is_valid': True})
            else:
                return JsonResponse({'postcode': f'{postcode}', 'is_valid': False})
        else:
            return JsonResponse({'error': 'No postcode provided'})
    else:
        return JsonResponse({'error': 'Only GET method is allowed'})
