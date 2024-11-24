import { useState } from "react";
import { fetchCalculateINsurance } from "../../services/insurance/fetchCalculateINsurance.ts";


export const useCalculateINsurance = () => {
  const [costInsurance, setCostInsurance] = useState<responseCalculateINsuranceeType | null>(null);
  const [error, setError] = useState<string | null>(null);

  const calculateInsurance = async (data: CalculateINsuranceType) => {
    try {
      const costInsuranceResponse = await fetchCalculateINsurance(data);
      setCostInsurance(costInsuranceResponse);
    } catch (err) {
      setError("Failed to fetch Calculate Insurance.");
      console.error(err);
    }
  };

  return { costInsurance, error, calculateInsurance };
};
