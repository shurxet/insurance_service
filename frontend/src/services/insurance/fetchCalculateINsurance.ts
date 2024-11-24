import apiClient from "../apiClient/apiClient.ts";


export const fetchCalculateINsurance = async (data: CalculateINsuranceType): Promise<responseCalculateINsuranceeType> => {

    try {
        const response = await apiClient.post<responseCalculateINsuranceeType>(
            '/insurance',
            data,
        );
        return response.data;
    } catch (error) {
        console.log((error as Error).message);
        throw error;
    }
};