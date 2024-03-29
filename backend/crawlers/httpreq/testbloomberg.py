import re

urls = [
    'https://www.bloomberg.com/lineup-next/api/page/markets-vp/module/pagination_story_list,pagination_rail_ad?moduleVariations=pagination,default&moduleTypes=story_list,ad&locale=en&publishedState=PUBLISHED',
    'https://www.bloomberg.com/lineup-next/api/page/economics-v2/module/quicktake,new_economy_video?moduleVariations=4_up_images,default&moduleTypes=story_package,video&locale=en&publishedState=PUBLISHED',
    'https://www.bloomberg.com/lineup-next/api/page/industries-v2/module/video?moduleVariations=default&moduleTypes=video&locale=en&publishedState=PUBLISHED',
]

pattern = r"/api/page/[^/]+/module/([^,?]+)"

extracted_parts = []
for url in urls:
    match = re.search(pattern, url)
    if match:
        extracted_parts.append(match.group(1))

print(extracted_parts)
