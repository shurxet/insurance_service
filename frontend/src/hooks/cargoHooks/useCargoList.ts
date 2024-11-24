import {useEffect, useState} from "react";
import {fetchCargoList, responseCargoListType} from "../../services/cargo/fetchCargoList.ts";

export const useCargoList = () => {
    const [cargos, setCargos] = useState<responseCargoListType>([]);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        (async () => {
            try {
                const cargoList = await fetchCargoList();
                setCargos(cargoList);
                console.log(cargoList);
            } catch (err) {
                setError('Failed to fetch cargoHooks list.');
                console.error(err);
            }
        })();
    }, []);

    return { cargos, error };
};
