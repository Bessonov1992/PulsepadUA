def create_body(pet_id=178, category_id=15, category_name='lizard', pet_name='Stepan', photo_urls=[
    'https://www.cali.gov.co/dagma/publicaciones/176508/la-fascinante-iguana-verde-caracteristicas'
    '-distribucion-y-su-rol-vital-en-los-ecosistemas/info/principal/media/pubInt/thumbs/thpub_700X400_176508.jpg'],
                tag_id=178, tag_name='beautiful iguana', status='available'):
    body = {
        'id': pet_id,
        'category': {
            'id': category_id,
            'name': category_name
        },
        'name': pet_name,
        'photoUrls': photo_urls,
        'tags': [
            {
                'id': tag_id,
                'name': tag_name
            }
        ],
        'status': status
    }
    return body
