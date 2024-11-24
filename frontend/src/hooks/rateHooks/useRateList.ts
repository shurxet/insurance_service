import {useEffect, useState} from "react";
import {fetchRateList, responseRateListType} from "../../services/rate/fetchRateList.ts";


export const useRateList = () => {
    const [rates, setRates] = useState<responseRateListType>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        (async () => {
            try {
                const rateList = await fetchRateList();
                setRates(rateList);
                console.log(rateList);
            } catch (err) {
                setError('Failed to fetch rateHooks list.');
                console.error(err);
            }
        })();
    }, []);

    return { rates, error };
};
