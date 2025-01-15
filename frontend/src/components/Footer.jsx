import React from 'react';
import { Box, Typography } from '@mui/material';

const Footer = () => (
  <Box mt={5} py={3} bgcolor="#f5f5f5" textAlign="center">
    <Typography variant="body2">
      © {new Date().getFullYear()} Tax Filing Company. All rights reserved.
    </Typography>
  </Box>
);

export default Footer;
