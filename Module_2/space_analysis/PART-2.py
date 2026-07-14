
import csv
#Time complexity: O(nlogn)
#Space complexity: O(n)
#Sorts the email and checks the neighbouring values

def find_duplicates_with_sort(file_name):
    emails = []
    duplicates = set()

    with open(file_name, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row['email'].strip().lower()
            emails.append(email)
    emails.sort()
    for i in range(1, len(emails)):
        if emails[i] == emails[i-1]:
            duplicates.add(emails[i])
    return duplicates
def main():
    filename = 'users.csv'
    print(find_duplicates_with_sort(filename))
#Time complexity: O(n)
#Space complexity: O(n)
#Uses set for fast look up but uses more memory
def find_duplicates_with_set(file_name):
    seen = set()
    duplicates = set()
    with open(file_name, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            email = row['email'].strip().lower()
            if email in seen:
                duplicates.add(email)
            else:
                seen.add(email)
    return duplicates

def main():
    filename = 'users.csv'

    set_duplicates = find_duplicates_with_set(filename)
    print("Duplicates found using a set:")
    print(set_duplicates)

    sort_duplicates = find_duplicates_with_sort(filename)
    print("\nDuplicates found using sorting:")
    print(sort_duplicates)
if __name__ == '__main__':
    main()
""" 4 GB RAM """
#I will use the sorting method. A set containing million of email strings can easily consume several gigabytes because each string and set entry has memory overhead.
""" 64 GB RAM """
#I will use the set approach, it will be much faster and 64 gb is likely enough.

        
