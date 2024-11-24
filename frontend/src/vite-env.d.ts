/// <reference types="vite/client" />


interface CargoType {
  id: number;
  name: string;
}

interface CargoListType {
  id: number;
  name: string;
}

interface CalculateINsuranceType {
  cargo_type: string,
  declared_value: number,
  date: string
}

interface responseCalculateINsuranceeType {
  insurance_cost: number
}

interface RateType {
  rate: number,
  effective_date: string,
  id: 1,
  cargo: CargoType
}
