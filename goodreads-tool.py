import csv
from collections import defaultdict

def rank_authors_by_pages(csv_file):
    author_pages = defaultdict(int)
    
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            exclusive_shelf = row['Exclusive Shelf']
            
            # Only process books on the "read" shelf
            if exclusive_shelf.lower() == 'read':
                author = row['Author']
                pages = row['Number of Pages']
                read_count = row['Read Count']
                
                if pages and read_count:
                    try:
                        total_pages = int(pages) * int(read_count)
                        author_pages[author] += total_pages
                    except ValueError:
                        pass  # Skip rows with non-numeric values
    
    # Sort authors by page count in descending order
    ranked_authors = sorted(author_pages.items(), key=lambda x: x[1], reverse=True)
    return ranked_authors

# Usage
csv_file = ''  # Your file path
result = rank_authors_by_pages(csv_file)

# Print the ranked results
print("Authors ranked by total pages read:") #multiplies the number of times read by the page count
for rank, (author, pages) in enumerate(result, 1):
    print(f"{rank}. {author}: {pages} pages")

# Print the total number of authors and pages
total_authors = len(result)
total_pages = sum(pages for _, pages in result)
print(f"\nTotal authors: {total_authors}")
print(f"Total pages read: {total_pages}")
