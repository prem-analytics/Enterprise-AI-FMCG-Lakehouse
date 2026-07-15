# Master Tables

Master tables store relatively stable business information. They are referenced by transaction tables using primary and foreign keys.

| Table | Target Rows | Purpose |
|--------|------------:|---------|
| Customers | 100,000 | Customer master |
| Products | 5,000 | Product master |
| Stores | 1,000 | Retail store master |
| Warehouses | 100 | Warehouse master |
| Factories | 10 | Manufacturing plant master |
| Suppliers | 250 | Supplier master |
| Employees | 5,000 | Employee master |

# Transaction Tables

Transaction tables capture day-to-day business activities.

| Table | Target Rows | Purpose |
|--------|------------:|---------|
| Sales | 5,000,000+ | Customer sales transactions |
| Inventory | 1,000,000+ | Inventory movements |
| Purchase Orders | 500,000+ | Supplier purchase orders |
| Shipments | 500,000+ | Distribution and logistics |
| Production | 250,000+ | Manufacturing records |
| Marketing Campaigns | 10,000+ | Marketing performance |