import "./App.css";
import theme from "./theme/theme.ts";
import {useCargoList} from "./hooks/cargoHooks/useCargoList.ts";
import {useRateList} from "./hooks/rateHooks/useRateList.ts";
import {useCalculateINsurance} from "./hooks/insuranceHooks/useCalculateINsurance.ts";
import {useState} from "react";

import {
    Alert,
    Box,
    Button,
    Card,
    CardContent,
    Container,
    CssBaseline,
    Divider,
    MenuItem,
    Slide,
    Stack,
    TextField,
    ThemeProvider,
    Typography,
} from "@mui/material";
import {LocalShipping} from "@mui/icons-material";

function App() {
  const { cargos } = useCargoList();
  const { rates } = useRateList();
  const { costInsurance, error, calculateInsurance } = useCalculateINsurance();
  const [formData, setFormData] = useState({
    cargo_type: "",
    declared_value: 0,
    date: "",
  });

  const getUniqueDates = (rates: { effective_date: string }[]) => {
      return Array.from(new Set(rates.map((rate) => rate.effective_date)));
  };

  const uniqueDates = getUniqueDates(rates);

  const handleSubmit = (e: { preventDefault: () => void; }) => {
    e.preventDefault();
    calculateInsurance(formData);
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box
        sx={{
          minHeight: "100vh",
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          background: "linear-gradient(135deg, #f5f7fa, #e1e8ed)",
          padding: 2,
        }}
      >
        <Container
          maxWidth="sm"
          sx={{
            padding: 4,
            background: "white",
            borderRadius: "16px",
            boxShadow: "0px 20px 50px rgba(0, 0, 0, 0.15)",
            "&:hover": {
              boxShadow: "0px 30px 60px rgba(0, 0, 0, 0.25)",
              transform: "scale(1.02)",
            },
            transition: "all 0.3s ease",
          }}
        >
          <Slide direction="down" in={true} timeout={600}>
            <Stack spacing={4} alignItems="center">
              <Typography
                variant="h3"
                component="h1"
                sx={{
                  fontWeight: 800,
                  textAlign: "center",
                  color: "#334155",
                  fontSize: { xs: "2rem", md: "2.5rem" },
                  letterSpacing: "0.1rem",
                  lineHeight: 1.2,
                }}
              >
                Онлайн сервис по страхованию груза
              </Typography>
              <Card
                sx={{
                  padding: 4,
                  borderRadius: "20px",
                  background: "linear-gradient(145deg, #ffffff, #f3f4f6)",
                  boxShadow:
                    "inset 5px 5px 10px #d4d4d8, inset -5px -5px 10px #ffffff",
                }}
              >
                <CardContent>
                  <Stack spacing={4}>
                    <Typography
                      variant="h5"
                      component="h2"
                      sx={{
                        textAlign: "center",
                        fontWeight: 700,
                        display: "flex",
                        alignItems: "center",
                        gap: 1,
                        fontSize: "1.5rem",
                        color: "#64748b",
                      }}
                    >
                      <LocalShipping sx={{ color: "#3b82f6" }} />
                      Расчёт стоимости страховки
                    </Typography>
                    <Divider />
                    <form onSubmit={handleSubmit}>
                      <Stack spacing={3}>
                        <TextField
                          select
                          label="Тип груза"
                          value={formData.cargo_type}
                          onChange={(e) =>
                            setFormData((prev) => ({
                              ...prev,
                              cargo_type: e.target.value,
                            }))
                          }
                          fullWidth
                          variant="outlined"
                          sx={{
                            "& .MuiOutlinedInput-root": {
                              borderRadius: "12px",
                            },
                          }}
                        >
                          <MenuItem value="">
                            <em>Выберите тип груза</em>
                          </MenuItem>
                          {cargos.map((cargo, index) => (
                            <MenuItem key={index} value={cargo.name}>
                              {cargo.name}
                            </MenuItem>
                          ))}
                        </TextField>

                        <TextField
                          select
                          label="Дата тарифа"
                          value={formData.date}
                          onChange={(e) =>
                            setFormData((prev) => ({
                              ...prev,
                              date: e.target.value,
                            }))
                          }
                          fullWidth
                          variant="outlined"
                          sx={{
                            "& .MuiOutlinedInput-root": {
                              borderRadius: "12px",
                            },
                          }}
                        >
                          <MenuItem value="">
                            <em>Выберите дату тарифа</em>
                          </MenuItem>
                          {uniqueDates.map((date, index) => (
                            <MenuItem key={index} value={date}>
                              {date}
                            </MenuItem>
                          ))}
                        </TextField>

                        <TextField
                          label="Объявленная стоимость"
                          type="number"
                          value={formData.declared_value || ""}
                          onChange={(e) =>
                            setFormData((prev) => ({
                              ...prev,
                              declared_value: e.target.value
                                ? Number(e.target.value)
                                : 0,
                            }))
                          }
                          fullWidth
                          variant="outlined"
                          sx={{
                            "& .MuiOutlinedInput-root": {
                              borderRadius: "12px",
                            },
                          }}
                        />

                        <Button
                          type="submit"
                          variant="contained"
                          fullWidth
                          sx={{
                            padding: "14px",
                            fontWeight: 700,
                            fontSize: "1.1rem",
                            borderRadius: "12px",
                            textTransform: "none",
                            background: "linear-gradient(135deg, #3b82f6, #2563eb)",
                            "&:hover": {
                              background: "linear-gradient(135deg, #2563eb, #1e40af)",
                            },
                          }}
                        >
                          Рассчитать
                        </Button>
                      </Stack>
                    </form>
                    {costInsurance && (
                      <Alert
                        severity="success"
                        sx={{
                          marginTop: 3,
                          background: "#d1fae5",
                          color: "#065f46",
                          borderRadius: "12px",
                        }}
                      >
                        <Typography variant="body1">
                          <strong>Стоимость страховки:</strong>{" "}
                          {costInsurance.insurance_cost} ₽
                        </Typography>
                      </Alert>
                    )}
                    {error && (
                      <Alert
                        severity="error"
                        sx={{
                          marginTop: 3,
                          background: "#fee2e2",
                          color: "#991b1b",
                          borderRadius: "12px",
                        }}
                      >
                        <Typography variant="body1">{error}</Typography>
                      </Alert>
                    )}
                  </Stack>
                </CardContent>
              </Card>
            </Stack>
          </Slide>
        </Container>
      </Box>
    </ThemeProvider>
  );
}

export default App;
