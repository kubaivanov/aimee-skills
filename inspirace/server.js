const express = require('express');
const fs = require('fs');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3000;

// Prevent indexing by search engines and bots - add headers to all responses
app.use((req, res, next) => {
    res.setHeader('X-Robots-Tag', 'noindex, nofollow, noarchive, nosnippet, noimageindex');
    next();
});

// Serve static files
app.use(express.static(__dirname));

// API: Get list of images from reklamy folder
app.get('/api/reklamy', (req, res) => {
    const reklamyDir = path.join(__dirname, 'reklamy');
    
    try {
        const files = fs.readdirSync(reklamyDir);
        const images = files.filter(file => {
            const ext = path.extname(file).toLowerCase();
            return ['.jpg', '.jpeg', '.png', '.gif', '.webp'].includes(ext);
        });
        res.json(images);
    } catch (error) {
        console.error('Error reading reklamy directory:', error);
        res.status(500).json({ error: 'Failed to read reklamy directory' });
    }
});

// API: Get list of copy files and their content
app.get('/api/copy', (req, res) => {
    const copyDir = path.join(__dirname, 'copy');
    
    try {
        const files = fs.readdirSync(copyDir);
        const mdFiles = files.filter(file => path.extname(file).toLowerCase() === '.md');
        
        const allHeadlines = [];
        
        mdFiles.forEach(file => {
            const filePath = path.join(copyDir, file);
            const content = fs.readFileSync(filePath, 'utf-8');
            
            // Parse markdown headlines (## N. Text format)
            const headlineRegex = /^## \d+\. (.+)$/gm;
            let match;
            while ((match = headlineRegex.exec(content)) !== null) {
                allHeadlines.push(match[1].trim());
            }
        });
        
        res.json(allHeadlines);
    } catch (error) {
        console.error('Error reading copy directory:', error);
        res.status(500).json({ error: 'Failed to read copy directory' });
    }
});

app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});
