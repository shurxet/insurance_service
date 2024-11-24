import apiClient from '../apiClient/apiClient.ts';


export type responseRateListType = RateType[];

export const fetchRateList = async (): Promise<responseRateListType> => {
    try {
        const response = await apiClient.get<responseRateListType>('/rate/');
        return response.data;
    } catch (error) {
        console.log((error as Error).message);
        throw error;
    }
};
