🏎️ Luxury Automotive Market Intelligence Dashboard
Competitive intelligence platform analyzing 530K+ transactions across premium automotive segments
Show Image
Show Image
Show Image
🎯 Project Overview
This interactive dashboard provides comprehensive market intelligence for the luxury automotive sector, with a focus on competitive analysis for premium brands like Porsche, Mercedes-Benz, BMW, and Audi. Built to demonstrate product analytics and strategic marketing capabilities for automotive industry positions.
Business Context
Created as part of application materials for Porsche Engineering Services Marketing & Strategy internship. Demonstrates:

Strategic market analysis
Competitive intelligence gathering
Data-driven decision making
Product positioning insights
Geographic market analysis

📊 Key Features
1. Executive Dashboard

Real-time KPIs for luxury automotive segment
Market share analysis (luxury vs mass market)
Premium pricing metrics
Transaction volume tracking

2. German Luxury Trio Analysis
Deep dive into Porsche's main competitors:

Mercedes-Benz, BMW, Audi comparison
Price positioning analysis
Volume and market share trends
Year-over-year performance tracking

3. Geographic Intelligence

State-by-state transaction volume
Luxury market penetration rates
Regional opportunity identification
Market concentration analysis

4. Performance Metrics

Engine specifications comparison
Horsepower distribution analysis
Price vs performance positioning
Technical differentiation insights

5. Strategic Recommendations

Market opportunity identification
Competitive positioning insights
Growth driver analysis
Actionable business intelligence

🚀 Quick Start
Prerequisites
bashPython 3.8+
pip package manager
Installation

Clone the repository

bashgit clone https://github.com/andrrresj/automotive-market-dashboard.git
cd automotive-market-dashboard

Install dependencies

bashpip install -r requirements.txt

Download datasets

Vehicle Sales Data → Save as car_prices.csv
Car Specifications Data → Save as data.csv
Place both files in project root directory


Clean the data

bashpython clean_data.py
This creates sales_cleaned.csv and specs_cleaned.csv

Launch dashboard

bashstreamlit run dashboard.py
Dashboard opens automatically at http://localhost:8501
📁 Project Structure
automotive-market-dashboard/
│
├── dashboard.py              # Main Streamlit dashboard
├── clean_data.py            # Data cleaning pipeline
├── explore_data.py          # Initial data exploration
│
├── car_prices.csv           # Raw sales data (not in repo)
├── data.csv                 # Raw specs data (not in repo)
├── sales_cleaned.csv        # Cleaned sales (generated)
├── specs_cleaned.csv        # Cleaned specs (generated)
│
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore rules
└── README.md               # This file
📈 Data Pipeline
1. Data Exploration (explore_data.py)

Loads raw datasets
Analyzes data quality and structure
Identifies key variables
Validates data completeness

2. Data Cleaning (clean_data.py)
Sales Data (558K → 530K rows):

Removes missing critical fields (make, price, year)
Filters realistic price range ($1K - $200K)
Focuses on modern vehicles (2000+)
Creates luxury brand flags
Categorizes by brand segment

Specifications Data (11.9K → 9.8K rows):

Removes incomplete records
Validates MSRP ranges
Enriches with market categories
Adds performance flags

3. Dashboard (dashboard.py)

Interactive visualizations
Real-time filtering
Multi-dimensional analysis
Strategic insights generation

🎨 Dashboard Sections
Executive Summary

Total Transactions: 530,243 sales analyzed
Luxury Segment: 95,621 premium vehicles (18.0%)
German Luxury: 42,884 Mercedes/BMW/Audi units
Average Luxury Price: $19,912 (56% premium over market)

Market Overview

Market share visualization by brand category
Price positioning across segments
Luxury vs mass market dynamics

German Luxury Deep Dive

Brand-by-brand comparison (Mercedes, BMW, Audi)
Price distribution analysis
Volume trends over time
Competitive positioning

Geographic Analysis

Top 10 states by transaction volume
Luxury market penetration by region
Geographic opportunity mapping

Performance Metrics

Horsepower distribution by brand
Price vs performance scatter analysis
Technical specifications comparison

Strategic Insights

Market opportunity identification
Competitive landscape assessment
Growth driver analysis
Actionable recommendations

💡 Key Insights
Market Dynamics

German luxury brands command 56% price premium over mass market
California, Texas, Florida drive 45% of luxury transactions
BMW leads in volume; Mercedes-Benz commands price premium
Average luxury vehicle age: 6.2 years

Competitive Landscape

Mercedes-Benz: Premium positioning, highest average price
BMW: Volume leader, performance heritage
Audi: Technology-forward, younger demographic appeal

Strategic Opportunities

Geographic Expansion: Untapped luxury markets in mountain states
Product Mix: Growing SUV segment within luxury category
Electric Transition: Opportunity for differentiation
Digital Commerce: Rising online transaction preference

🎯 Skills Demonstrated
Technical Skills

Data Analysis: Pandas, NumPy for large dataset manipulation
Visualization: Plotly for interactive charts and dashboards
Web Apps: Streamlit for professional dashboard deployment
Data Cleaning: ETL pipeline development
Python: Advanced programming and libraries

Business Skills

Strategic Analysis: Competitive intelligence and market positioning
Product Thinking: Understanding customer segments and needs
Communication: Translating data into actionable insights
Industry Knowledge: Automotive market dynamics and trends

Analytical Capabilities

Market segmentation and targeting
Competitive benchmarking
Geographic market analysis
Price optimization insights
Performance metrics tracking

## 📸 Dashboard Screenshots

### Executive Dashboard Overview
![Dashboard Overview](https://github.com/user-attachments/assets/5bc20b6e-1398-4f64-8340-3fa006578457)
*Real-time KPIs and market segmentation analysis*

### Market Overview
![Market Overview](https://github.com/user-attachments/assets/1e13d1ea-29d5-44dd-80c2-7febc80a6e82)
*Luxury Automotive Market vs Mass Automotive Market*

### Luxury Competitive Analysis
![German Luxury Analysis](https://github.com/user-attachments/assets/1e13d1ea-29d5-44dd-80c2-7febc80a6e82)
*Mercedes-Benz, BMW, and Audi comparison with price trends*

### Geographic Market Intelligence
![Geographic Analysis](https://github.com/user-attachments/assets/54bde31d-7b18-4ff3-ba96-ab09b43716e2)
*State-level transaction volume and luxury penetration rates*

### Performance Metrics
![Performance Metrics](https://github.com/user-attachments/assets/d1a9ed26-ea00-4f7a-82f8-9b320ee2a52b)
*Engine specifications and price vs performance positioning*

### Strategic Insights
![Strategic Insights](https://github.com/user-attachments/assets/2328042b-ad23-47aa-bddb-7081860aab68)
*Market opportunities and competitive recommendations*

---

📊 Data Sources

Vehicle Sales Data: 558,837 real automotive transactions

Source: Kaggle - Vehicle Sales Data
Years: 2000-2024
Geographic: US state-level data


Car Specifications: 11,914 vehicle models

Source: Kaggle - Car Dataset
Includes: Engine specs, pricing, features
Coverage: Major automotive brands



🔮 Future Enhancements

 Add predictive pricing models
 Implement customer segmentation (RFM analysis)
 Include electric vehicle trend analysis
 Add time-series forecasting
 Integrate social media sentiment data
 Deploy to cloud (Streamlit Cloud)
 Add PDF report generation
 Include lease vs purchase analysis

🎓 Application Context
Porsche Engineering Services Internship
This project directly addresses key requirements:

✅ Marketing Analytics: Competitive intelligence and market analysis
✅ Strategic Thinking: Market positioning and opportunity identification
✅ Data Analysis: Large dataset manipulation and insights generation
✅ Business Acumen: Understanding luxury automotive market dynamics
✅ Communication: Clear visualization of complex data
✅ Industry Passion: Genuine interest in automotive sector

Transferable to Other Industries
The analytical framework applies to:

Consumer electronics (Apple, Samsung ecosystem)
Fashion/luxury goods (premium brand positioning)
Real estate (market segmentation and pricing)
SaaS products (tiered pricing analysis)

👤 Author
Andres Jimenez

GitHub: @andrrresj
LinkedIn: Andres Jimenez
Portfolio: View Projects

Additional Context

Background: Economics & International Business, SDSU
Interests: Healthcare analytics, automotive industry, data visualization
Side Business: Car photography business (combines passion with business)
Career Goal: Product analytics role at tech/automotive company

📄 License
This project is open source and available under the MIT License.
🙏 Acknowledgments

Data provided by Kaggle community datasets
Built as demonstration of analytics capabilities for Porsche internship application
Inspired by real-world automotive market intelligence needs
Special thanks to the automotive data science community

📞 Contact
For questions about this project or collaboration opportunities:

LinkedIn: Connect with me
GitHub Issues: Report bugs or request features


⭐ If you find this project useful for your own automotive analytics work, please consider starring the repository!
Last updated: November 2025
