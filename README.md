# TaiwanViz

TaiwanViz is a comprehensive Python library and web API for creating interactive visualizations and maps of Taiwan. The project provides tools for generating choropleth maps, analyzing geographical data, and serving map-based applications through a FastAPI web interface.

## Features

The library offers extensive capabilities for Taiwan geographical data visualization including support for multiple administrative levels (county, town, village), customizable color palettes and styling options, comprehensive font support for Traditional Chinese characters, flexible data input handling, and choropleth map generation with various configuration options. The FastAPI-based web API provides RESTful endpoints for map generation and metadata retrieval.

## Project Structure

```bash
.
├── Makefile
├── api
│   ├── main.py
│   ├── routers
│   │   ├── maps.py
│   │   └── meta.py
│   ├── schemas.py
│   └── startup.py
├── poetry.lock
├── pyproject.toml
└── taiwanviz
    ├── __init__.py
    ├── data
    │   └── shp
    │       ├── county
    │       │   ├── COUNTY_MOI_1140318.CPG
    │       │   ├── COUNTY_MOI_1140318.dbf
    │       │   ├── COUNTY_MOI_1140318.prj
    │       │   ├── COUNTY_MOI_1140318.sbn
    │       │   ├── COUNTY_MOI_1140318.sbx
    │       │   ├── COUNTY_MOI_1140318.shp
    │       │   ├── COUNTY_MOI_1140318.shp.xml
    │       │   ├── COUNTY_MOI_1140318.shx
    │       │   └── TW-01-301000100G-000017.xml
    │       ├── town
    │       │   ├── TOWN_MOI_1140318.CPG
    │       │   ├── TOWN_MOI_1140318.dbf
    │       │   ├── TOWN_MOI_1140318.prj
    │       │   ├── TOWN_MOI_1140318.sbn
    │       │   ├── TOWN_MOI_1140318.sbx
    │       │   ├── TOWN_MOI_1140318.shp
    │       │   ├── TOWN_MOI_1140318.shp.xml
    │       │   ├── TOWN_MOI_1140318.shx
    │       │   ├── TW-07-301000100G-614001.xml
    │       │   ├── Town_Majia_Sanhe.CPG
    │       │   ├── Town_Majia_Sanhe.dbf
    │       │   ├── Town_Majia_Sanhe.prj
    │       │   ├── Town_Majia_Sanhe.sbn
    │       │   ├── Town_Majia_Sanhe.sbx
    │       │   ├── Town_Majia_Sanhe.shp
    │       │   ├── Town_Majia_Sanhe.shp.xml
    │       │   └── Town_Majia_Sanhe.shx
    │       └── village
    │           ├── TW-07-301000100G-613995.xml
    │           ├── VILLAGE_NLSC_1140825.CPG
    │           ├── VILLAGE_NLSC_1140825.dbf
    │           ├── VILLAGE_NLSC_1140825.prj
    │           ├── VILLAGE_NLSC_1140825.shp
    │           ├── VILLAGE_NLSC_1140825.shx
    │           ├── Village_Sanhe.CPG
    │           ├── Village_Sanhe.dbf
    │           ├── Village_Sanhe.prj
    │           ├── Village_Sanhe.shp
    │           └── Village_Sanhe.shx
    ├── data_loader.py
    ├── fonts
    │   ├── cwTeX
    │   │   ├── cwTeXQHeiZH-Bold.ttf
    │   │   ├── cwTeXQKaiZH-Medium.ttf
    │   │   ├── cwTeXQMingZH-Medium.ttf
    │   │   └── cwTeXQYuanZH-Medium.ttf
    │   └── noto-sans
    │       ├── NotoSansTC-Black.ttf
    │       ├── NotoSansTC-Bold.ttf
    │       ├── NotoSansTC-ExtraBold.ttf
    │       ├── NotoSansTC-ExtraLight.ttf
    │       ├── NotoSansTC-Light.ttf
    │       ├── NotoSansTC-Medium.ttf
    │       ├── NotoSansTC-Regular.ttf
    │       ├── NotoSansTC-SemiBold.ttf
    │       └── NotoSansTC-Thin.ttf
    ├── models
    │   ├── __init__.py
    │   ├── base
    │   │   ├── __init__.py
    │   │   ├── base.py
    │   │   └── layers.py
    │   ├── choropleth.py
    │   ├── config
    │   │   ├── __init__.py
    │   │   └── render_config.py
    │   ├── data_input.py
    │   ├── enums
    │   │   ├── __init__.py
    │   │   └── enums.py
    │   └── palette
    │       ├── __init__.py
    │       └── palette.py
    ├── notebook
    │   └── main.ipynb
    └── utils
        ├── __init__.py
        ├── colors.py
        ├── filters.py
        ├── fonts.py
        └── plotting.py
```

The project is organized into several key components. The api directory contains the FastAPI application with main.py as the entry point, routers for maps and metadata endpoints, schema definitions, and startup configuration. The taiwanviz directory houses the core library including data loaders, model definitions, utility functions, and geographical data files.

The data directory contains shapefiles for Taiwan's administrative boundaries organized by county, town, and village levels with official MOI (Ministry of the Interior) boundary data. Font resources include both cwTeX and Noto Sans Traditional Chinese font families for proper text rendering in visualizations.

The models package provides base classes and layers for map generation, choropleth map implementations, configuration management, data input handling, enumeration definitions, and color palette management. Utility modules offer color manipulation functions, data filtering capabilities, font management, and plotting utilities.

## Installation

The project uses Poetry for dependency management. To set up the development environment, first ensure you have Python 3.8 or higher and Poetry installed on your system.

Clone the repository and navigate to the project directory. Install the project dependencies using Poetry by running the install command. This will create a virtual environment and install all required packages including their development dependencies.

```bash
poetry install
```

## Usage

### Running the Web API

To start the FastAPI web server for development, use the provided Makefile command. The API will be available at http://localhost:8000 with automatic reload enabled for development.

```bash
make web
```

Alternatively, you can run the server directly using uvicorn with Poetry.

### Development Commands

The project includes several useful development commands accessible through the Makefile. Format your code using autoflake, isort, and black for consistent styling. Run linting checks using flake8 to ensure code quality. Execute the test suite using pytest with optional arguments. Use pytest-watch for continuous testing during development. Generate coverage reports to monitor test coverage. Clean up temporary files and caches when needed. Generate a project tree structure for documentation purposes.

```bash
make fmt      # Format code
make lint     # Run linting
make test     # Run tests
make ptw      # Run tests with watch mode
make coverage # Generate coverage report
make clean    # Clean temporary files
make tree     # Generate project structure
```

### Library Usage

The TaiwanViz library can be imported and used programmatically for creating custom visualizations. The library provides comprehensive support for loading Taiwan geographical data, creating choropleth maps with custom data, configuring visual styling and color schemes, handling various data input formats, and exporting maps in multiple formats.

Import the necessary modules from the taiwanviz package to access data loading capabilities, map generation functions, and configuration options. The data loader module provides functions to load shapefile data for different administrative levels. Model classes offer structured approaches to map creation with customizable parameters.

### API Endpoints

The FastAPI application exposes several endpoints for map generation and data retrieval. Map-related endpoints allow for dynamic map generation with custom parameters, data overlay capabilities, and various output formats. Metadata endpoints provide information about available geographical boundaries, administrative divisions, and supported data formats.

The API documentation is automatically generated and available at the /docs endpoint when running the development server. This interactive documentation allows for easy testing and exploration of available endpoints and their parameters.

## Configuration

The project supports extensive configuration options for map rendering, data processing, and API behavior. Configuration files are located in the models/config directory and provide settings for default map styling, color palette definitions, font preferences, data processing parameters, and output format options.

Render configuration allows customization of map appearance including color schemes, font selection, layout parameters, and styling options. Data input configuration handles various data formats and processing rules. API configuration manages server behavior, endpoint settings, and response formatting.

## Data Sources

TaiwanViz includes official geographical boundary data from Taiwan's government sources through the National Land Surveying and Mapping Center (NLSC) open data platform. All geographical data is sourced from the official MOI (Ministry of the Interior) [open data repository](https://whgis-nlsc.moi.gov.tw/Opendata/Files.aspx).

The data includes:

County-level boundaries using the COUNTY_MOI_1140318 dataset providing accurate administrative boundaries for all counties and cities in Taiwan. Town-level data includes comprehensive township and district boundaries (TOWN_MOI_1140318) with special handling for indigenous areas including supplementary data for Majia and Sanhe townships. Village-level boundaries (VILLAGE_NLSC_1140825) offer the most detailed administrative divisions available with additional specific boundary data for Sanhe village.

The shapefiles include complete attribute data for each administrative unit including official names in Traditional Chinese, administrative codes, area calculations, and hierarchical relationships between different levels of government. All data follows the official government standards and is regularly updated to reflect administrative changes.

## Font Support

The project includes comprehensive font support for Traditional Chinese text rendering. Two major font families are provided: cwTeX fonts offering Hei (sans-serif), Kai (script), Ming (serif), and Yuan (rounded) styles in appropriate weights; and Noto Sans Traditional Chinese fonts providing a complete range of weights from thin to black for consistent modern typography.

Font utilities in the project automatically handle font loading, character encoding, and text rendering for map labels and annotations. The font selection system ensures proper display of Traditional Chinese characters across different operating systems and environments.

## Development

The project follows modern Python development practices with comprehensive testing, code formatting, and quality assurance. The development workflow includes automated code formatting using black for consistent styling, import sorting with isort, unused import removal with autoflake, code quality checks with flake8, comprehensive test coverage with pytest, and continuous integration support.

Development dependencies include testing frameworks, code formatters, linting tools, and documentation generators. The project structure supports easy extension and modification with clear separation of concerns and modular design.

## Contributing

Contributions to TaiwanViz are welcome and should follow the established development practices. Ensure all code passes linting and formatting checks, includes appropriate test coverage, maintains compatibility with existing functionality, and includes proper documentation for new features.

The project uses Poetry for dependency management, so new dependencies should be added through Poetry commands. Code changes should be tested thoroughly and include both unit and integration tests where appropriate. Documentation should be updated to reflect new features or changes in functionality.

## License

This project includes geographical data from Taiwan government sources which may be subject to specific usage terms. Users should verify compliance with relevant data usage policies when using this library in commercial or public applications. The code components of the library are provided for educational and research purposes.

## Technical Requirements

TaiwanViz requires Python 3.8 or higher for compatibility with modern language features and libraries. Key dependencies include FastAPI for web API functionality, GeoPandas for geographical data processing, Matplotlib for visualization rendering, Poetry for dependency management, and Uvicorn for ASGI server functionality.

The library is designed to work across different operating systems with proper handling of file paths, font loading, and system-specific configurations. Performance optimization ensures efficient handling of large geographical datasets and rapid map generation for web applications.

## Support and Documentation

For detailed API documentation, visit the /docs endpoint when running the development server. The interactive documentation provides comprehensive information about available endpoints, request parameters, response formats, and example usage.

Additional examples and tutorials can be found in the notebook directory, which contains Jupyter notebooks demonstrating various library features and use cases. These notebooks serve as both documentation and testing environments for new functionality.