// theme.ts
import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#1976d2", // Синий основной цвет
    },
    secondary: {
      main: "#ff4081", // Розовый акцент
    },
    background: {
      default: "#f4f6f8", // Светлый фон по умолчанию
      paper: "#ffffff", // Белый фон для карточек и других элементов
    },
  },
  typography: {
    fontFamily: "'Roboto', sans-serif",
    h4: {
      fontWeight: 700,
      color: "#1976d2",
    },
    h6: {
      fontWeight: 600,
      color: "#424242",
    },
    body1: {
      fontWeight: 500,
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        contained: {
          borderRadius: "8px",
          transition: "background-color 0.3s ease",
          "&:hover": {
            backgroundColor: "#115293",
          },
        },
      },
    },
    MuiTextField: {
      styleOverrides: {
        root: {
          backgroundColor: "#ffffff",
          borderRadius: "8px",
        },
      },
    },
  },
});

export default theme;
