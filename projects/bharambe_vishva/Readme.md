# Project Title: Write your project name here

## Student Details
- **Name**: vishva vishal bharambe 
- **PRN**: 2570127104  
- **Year**: FY
- **Branch**: R&A 

---

## Problem Statement
In India, vehicle rental services are not widely available, and people often struggle when they need a temporary vehicle for travel. Buying a new vehicle is costly, while public transport is not always convenient. A rental system can solve this by making different types of vehicles easily available for short-term use at affordable rates.

---

## Features
List the main things your project can do.  
Example:  
- works on availibility system
- runs in very basic codes  
- Remind with notifications  
- Works offline 

---

## Tech Stack
List the tools or languages you used.  
Example: C language and chatgpt 

---

## How to Run
1. Open the folder in Code::blockes or any online compiler like programiz.  
2. Run ` main.c`  
3. The program will start in offline mode.

---

## Project Structure

/* made a project for my bike rental business which my father runs back in hometown  so idea is original*/
#include <stdio.h>
#include <string.h>

// Structure for Vehicle
struct Vehicle {
    int id;
    char type[200];
    char model[200];
    int available;
};

// Structure for rentals
struct Rental {
    int vehicleId;
    int hours;
    int days;
    int weeks;
    char customerName[50];
    char customerPhone[15];
};

int main() {
    // Vehicle database
    struct Vehicle vehicles[5] = {
        {1, "Car", "Suzuki Swift", 1},
        {2, "Car", "Hyundai i20", 1},
        {3, "Bike", "Yamaha R15", 1},
        {4, "Scooter", "Honda Activa", 1},
        {5, "Bike", "Royal Enfield", 1}
    };

    struct Rental rental = {0, 0, 0, 0, "", ""};
    int choice, vid;

    // Rates
    float hourly_rate = 100;   // ₹100 per hour
    float daily_rate  = 600;   // ₹600 per day
    float weekly_rate = 2500;  // ₹2500 per week

    do {
        printf("\n================ VEHICLE RENTAL SYSTEM ================\n");
        printf("1. View Available Vehicles\n");
        printf("2. Rent a Vehicle\n");
        printf("3. Return Vehicle\n");
        printf("4. Exit\n");
        printf("=======================================================\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("\n--- Available Vehicles ---\n");
                for(int i=0; i<5; i++) {
                    if(vehicles[i].available == 1)
                        printf("ID: %d | Type: %-7s | Model: %s\n",
                               vehicles[i].id, vehicles[i].type, vehicles[i].model);
                }
                break;

            case 2:
                printf("\nEnter Vehicle ID to Rent: ");
                scanf("%d", &vid);
                if(vid < 1 || vid > 5 || vehicles[vid-1].available == 0) {
                    printf("Invalid or unavailable vehicle!\n");
                } else {
                    vehicles[vid-1].available = 0;
                    rental.vehicleId = vid;

                    printf("Enter Customer Name: ");
                    getchar(); // clear newline
                    fgets(rental.customerName, 50, stdin);
                    rental.customerName[strcspn(rental.customerName, "\n")] = 0; // remove newline

                    printf("Enter Customer Phone: ");
                    scanf("%s", rental.customerPhone);

                    printf("Enter rental hours: ");
                    scanf("%d", &rental.hours);
                    printf("Enter rental days: ");
                    scanf("%d", &rental.days);
                    printf("Enter rental weeks: ");
                    scanf("%d", &rental.weeks);

                    printf("\n✅ %s %s rented successfully to %s!\n",
                           vehicles[vid-1].type, vehicles[vid-1].model, rental.customerName);
                }
                break;

            case 3:
                if(rental.vehicleId == 0) {
                    printf("No vehicle is currently rented!\n");
                } else {
                    float cost = rental.hours * hourly_rate +
                                 rental.days * daily_rate +
                                 rental.weeks * weekly_rate;
                    vehicles[rental.vehicleId - 1].available = 1;

                    printf("\n============== RENTAL RECEIPT ==============\n");
                    printf("Customer Name : %s\n", rental.customerName);
                    printf("Phone Number  : %s\n", rental.customerPhone);
                    printf("Vehicle Rented: %s %s\n",
                           vehicles[rental.vehicleId - 1].type, vehicles[rental.vehicleId - 1].model);
                    printf("Duration      : %d Hours, %d Days, %d Weeks\n",
                           rental.hours, rental.days, rental.weeks);
                    printf("-------------------------------------------\n");
                    printf("Rent to Pay   : ₹%.2f\n", cost);
                    printf("===========================================\n");

                    rental.vehicleId = 0; // reset
                }
                break;

            case 4:
                printf("\nThank you for using Vehicle Rental System! 🚗🛵\n");
                break;

            default:
                printf("Invalid choice!\n");
        }

    } while(choice != 4);

    return 0;
}


---

## Demo Screenshot / Output
added screenshot with files

---

## AI Tools Used
chatGPT

---

## Future Improvements
ill add more features and make an actual app


---

## Notes for Reviewers
Any extra note for the FOSS team.  
Example: "This project runs offline by default." or "Needs an internet connection."

---

## Submission Checklist 
- [x] Cloned the Repository 
- [ ] Added my details (Name, PRN, Year, Branch)  
- [ ] Wrote Problem Statement  
- [ ] Listed Features & Tech Stack  
- [ ] Added clear Run Instructions  
- [ ] Provided Demo Output (screenshot or text)  
- [ ] Listed AI tools used (or None)  
- [ ] Explained Future Improvements  
- [ ] Project runs offline

