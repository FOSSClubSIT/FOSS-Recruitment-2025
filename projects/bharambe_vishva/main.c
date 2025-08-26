#include <stdio.h>
#include <string.h>

// Structure for Vehicle
struct Vehicle {
    int id;
    char type[20];
    char model[20];
    int available;
};

// Structure for Rental
struct Rental {
    int vehicleId;
    int hours;
    int days;
    int weeks;
};

int main() {
    // Vehicle database
    struct Vehicle vehicles[5] = {
        {1, "Car", "Suzuki", 1},
        {2, "Car", "Hyundai", 1},
        {3, "Bike", "Yamaha", 1},
        {4, "Scooter", "Honda Activa", 1},
        {5, "Bike", "Royal Enfield", 1}
    };

    struct Rental rental = {0, 0, 0, 0};
    int choice, vid;

    // Rates
    float hourly_rate = 100;   // ₹100 per hour
    float daily_rate  = 600;   // ₹600 per day
    float weekly_rate = 2500;  // ₹2500 per week

    do {
        printf("\n========== VEHICLE RENTAL SYSTEM ==========\n");
        printf("1. View Available Vehicles\n");
        printf("2. Rent a Vehicle\n");
        printf("3. Return Vehicle\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                printf("\n--- Available Vehicles ---\n");
                for(int i=0; i<5; i++) {
                    if(vehicles[i].available == 1)
                        printf("ID: %d | Type: %s | Model: %s\n",
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
                    printf("Enter rental hours: ");
                    scanf("%d", &rental.hours);
                    printf("Enter rental days: ");
                    scanf("%d", &rental.days);
                    printf("Enter rental weeks: ");
                    scanf("%d", &rental.weeks);
                    printf("%s %s rented successfully!\n", vehicles[vid-1].type, vehicles[vid-1].model);
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
                    printf("\nVehicle Returned: %s %s\n",
                           vehicles[rental.vehicleId - 1].type, vehicles[rental.vehicleId - 1].model);
                    printf("Total Rental Cost: ₹%.2f\n", cost);
                    rental.vehicleId = 0;
                }
                break;

            case 4:
                printf("Exiting system. Thank you!\n");
                break;

            default:
                printf("Invalid choice!\n");
        }

    } while(choice != 4);

    return 0;
}
