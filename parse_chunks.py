from bs4 import BeautifulSoup

soup_chunk_1 = None
soup_chunk_2 = None
song_count_spofify = 61
song_counter = 1

# final_links_arr = "final_list_postpunk.txt"

# chunk_1_filename = "chunk_1_postpunk.html"
# chunk_2_filename = "chunk_2_postpunk.html"

# chunk_1_links = "chunk_1_postpunk.txt"
# chunk_2_links = "chunk_2_postpunk.txt"


final_links_arr = "final_list_postpunk.txt"

chunk_1_filename = "source/chunk_1_pospunk.html"
chunk_2_filename = "source/chunk_2_pospunk.html"

chunk_1_links = "source/chunk_1_pospunk.txt"
chunk_2_links = "source/chunk_2_pospunk.txt"


def read_html():
    global soup_chunk_1, soup_chunk_2

    with open(f"{chunk_1_filename}", "r") as read_chunk_1:
        chunk_1 = read_chunk_1.read()

    with open(f"{chunk_2_filename}", "r") as read_chunk_2:
        chunk_2 = read_chunk_2.read()

    soup_chunk_1 = BeautifulSoup(chunk_1, "lxml")
    soup_chunk_2 = BeautifulSoup(chunk_2, "lxml")

    return soup_chunk_1, soup_chunk_2

def find_all_hrefs(soup):
    hrefs = []
    links = soup.find_all('a', class_='btE2c3IKaOXZ4VNAb8WQ')
    for link in links:
        hrefs.append(link.get('href'))
    return hrefs

if __name__ == "__main__":

    soup_chunk_1, soup_chunk_2 = read_html()
    hrefs_chunk_1 = find_all_hrefs(soup_chunk_1)
    hrefs_chunk_2 = find_all_hrefs(soup_chunk_2)

    for href in hrefs_chunk_1:
        with open(f"{chunk_1_links}", 'a') as write_href_chunk_1:
            if hrefs_chunk_1.index(href) != (len(hrefs_chunk_1) -1):
                write_href_chunk_1.write(f"https://open.spotify.com{href}\n")
            else:
                write_href_chunk_1.write(f"https://open.spotify.com{href}")
            

    for href in hrefs_chunk_2:
        with open(f"{chunk_2_links}", 'a') as write_href_chunk_2:
            if hrefs_chunk_2.index(href) != (len(hrefs_chunk_2) -1):
                write_href_chunk_2.write(f"https://open.spotify.com{href}\n")
            else:
                write_href_chunk_2.write(f"https://open.spotify.com{href}")
    
    tracks_1 = None
    tracks_2 = None

    # Compare links 
    with open(f"{chunk_1_links}", 'r') as read_href_chunk_1:
        with open(f"{chunk_2_links}", 'r') as read_href_chunk_2:
            tracks_1 = read_href_chunk_1.read().split("\n")
            tracks_2 = read_href_chunk_2.read().split("\n")
    
    # print(*tracks_2, end="\n")
    final_tracks_list = []


    for compare_track in tracks_1:
        # for track in tracks_2:
        if compare_track not in final_tracks_list:
            final_tracks_list.append(compare_track)
    

    for compare_track in tracks_2:
        if compare_track not in final_tracks_list:
            final_tracks_list.append(compare_track)
    

    # Check result
    with open(f"{final_links_arr}", 'a') as check_result:
        for item in final_tracks_list:
            song_counter += 1
            if (song_counter - 1) <= song_count_spofify:
                check_result.write(f"{item}\n")                
    print()
