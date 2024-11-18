# Toto-jewelry - Web Application

## About the Project
A web application created for a handmade jewelry manufacturer, serving to showcase products and communicate with customers. The application enables management of products, categories, and blog through an administrative interface.

## Main Features

### Public Section
- Jewelry presentation in gallery with category filtering
- Detailed product view with images and videos
- "About Me" section with manufacturer information
- Blog section with articles and photo gallery
- Contact page
- Responsive design for all devices
- Advanced search functionality with real-time suggestions

### Administrative Section (CRUD Operations)

#### Product Management
- Adding new products
- Editing existing products
- Deleting products
- Setting product availability
- Uploading images and videos

#### Category Management
- Creating new categories
- Editing existing categories
- Deleting categories
- Assigning products to categories

#### Blog Management
- Adding new articles
- Editing existing articles
- Deleting articles
- Uploading multiple images for articles
- Automatic reading time calculation

### Enhanced Search Functionality
- Real-time search suggestions as user types
- Search across multiple content types (products, categories, blogs)
- Visual feedback with highlighted search terms
- Support for images and videos in search results
- Search history using localStorage
- Mobile-optimized search interface
- Debounced search requests for performance
- Relevance-based result ordering
- Rich media preview in suggestions
- Smooth animations for suggestion box
- Cross-model search capabilities

#### Search Implementation Details
- Frontend Features:
  - Real-time suggestions with debouncing
  - Highlighted search terms in results
  - Image and video preview support
  - Smooth animations for UI elements
  - Mobile-friendly interface
  - Search history management
  - Keyboard navigation support

- Backend Features:
  - Full-text search across multiple models
  - Relevance-based result ordering
  - Search in product names, descriptions, and categories
  - Blog content search capability
  - Efficient query optimization
  - Cross-model search integration

## Technical Details

### File Upload Limitations
- Images: maximum size 15 MB
- Videos: maximum size 120 MB

### SEO Optimization
- Meta tags for all pages
- Open Graph protocol for social media sharing
- Schema.org markup for better indexing
- Optimized URLs (slugs)

### Security
- User authentication for admin functions
- CSRF protection for all forms
- File upload validation

### Pagination and Filtering
- Adjustable items per page (15/30/50)
- Product filtering by categories
- Direct page navigation

## Technologies Used
- Django (Python web framework)
- HTML5, CSS3, JavaScript
- PostgreSQL database

## Server Environment

### Hosting Infrastructure
- VPS (Virtual Private Server)
- Operating System: Ubuntu Linux 22.04 LTS
- Web Server: Nginx 1.18
- WSGI Server: Gunicorn 20.1
- Database: PostgreSQL 14

### Server Configuration
- Nginx as reverse proxy
- Gunicorn WSGI server with 4 workers
- Automatic SSL certificate management via Let's Encrypt
- Gzip compression for static files
- Static content caching
- Optimized Django application settings

### Security Features
- Custom security middleware with:
  - IP filtering
  - Request pattern validation
  - Port restriction
  - Host validation
  - User agent verification
- HTTPS enforcement
- HSTS implementation
- XSS protection
- Content type sniffing prevention
- Rate limiting for API endpoints
- CSRF protection
- Secure cookie configuration

### Monitoring and Performance
- Sentry integration for error tracking and performance monitoring
- Automated database backups
- UFW firewall configuration
- DDoS protection
- Regular security updates
- Comprehensive logging system

### Performance Optimization
- Application-level caching
- Database query optimization
- CDN integration for static files
- Lazy loading for images and videos
- CSS and JavaScript minification
- Template caching
- Optimized media file processing

### Analytics and Tracking
- Google Analytics integration
- Custom event tracking
- User behavior analytics
- Performance metrics monitoring

