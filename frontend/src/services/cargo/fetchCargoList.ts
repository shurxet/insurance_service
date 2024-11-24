import apiClient from '../apiClient/apiClient.ts';


export type responseCargoListType = CargoListType[];

export const fetchCargoList = async (): Promise<responseCargoListType> => {
    try {
        const response = await apiClient.get<responseCargoListType>('/cargo/');
        return response.data;
    } catch (error) {
        console.log((error as Error).message);
        throw error;
    }
};
